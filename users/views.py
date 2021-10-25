from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import logout, authenticate, login
from users.forms import CustomUserCreationForm
from django.shortcuts import reverse
from django.shortcuts import render, get_object_or_404
from users.models import CustomUser
from users.forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from decimal import Decimal
from cake.models import Promo
from django.conf import settings
from django.utils import timezone
from cake.models import Param


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(
                username=new_user.username,
                password=request.POST['password1']
                )
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('login'))
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def get_order_price(order):

    # if params are not specified use defaults
    writing_price = Decimal(0)
    express_delivery_koef = Decimal(1)

    params = Param.objects.filter(
        param_name__in=('WRITING_PRICE', 'EXPRESS_DELIVERY_KOEF')
        )

    for param in params:
        if param.param_name == 'WRITING_PRICE':
            writing_price = Decimal(param.param_value)
        if param.param_name == 'EXPRESS_DELIVERY_KOEF':
            express_delivery_koef = Decimal(param.param_value)

    if order.fixed_price == 0:
        order_price = 0

    for berry in order.berry.all():
        order_price += berry.price

    for dec in order.decoration.all():
        order_price += dec.price

    for top in order.topping.all():
        order_price += top.price

    order_price += order.layer.price
    order_price += order.form.price

    # check writing
    if order.writing:
        order_price += writing_price

    # check promocode
    promo = Promo.objects.filter(
        name=order.promocode, active=True
    ).order_by('-id').last()
    if promo:
        order_price = order_price * (
            (100 - promo.discont_percent) / Decimal(100)
        )

    # check date
    delta = order.delivery_at - timezone.now()
    if delta.days >= 0 and delta.days <= 1:
        order_price = order_price * express_delivery_koef

    return order_price


def serialize_order(order):

    patterns = {
        'форма': [],
        'слоев': [],
        'ягоды': [],
        'декор': [],
        'топпинг': [],
        'надпись': []
    }

    for berry in order.berry.all():
        patterns['ягоды'].append(berry.name)

    for dec in order.decoration.all():
        patterns['декор'].append(dec.name)

    for top in order.topping.all():
        patterns['топпинг'].append(top.name)

    patterns['слоев'].append(order.layer.num)
    patterns['форма'].append(order.form.name)

    if order.writing:
        patterns['надпись'].append(order.writing)
    order.patterns = patterns

    return {
        'id': order.id,
        'status': order.get_status_display(),
        'price': order.fixed_price,
        'fullname': f'{order.customer.first_name} \
            {order.customer.last_name}',
        'comment': order.comment,
        'patterns': order.patterns,
        'customer': order.customer,
        'delivery_at': order.delivery_at,
    }


@login_required(login_url='/users/login/')
def profile(request, pk):
    user = get_object_or_404(CustomUser, id=pk)

    orders = list(user.orders.exclude(status='CANCELLED')
        .select_related('layer', 'form')
        .prefetch_related('berry', 'decoration', 'topping')
        .order_by('delivery_at', '-id'))

    serialized_orders = [serialize_order(order) for order in orders]

    paginator = Paginator(serialized_orders, settings.ITEMS_PER_PAGE)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if user != request.user:
        raise Http404

    if request.method != 'POST':
        form = CustomUserChangeForm(instance=user)
    else:
        form = CustomUserChangeForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile', args=[user.id]))

    context = {
        'page_obj': page,
        'user_form': form,
        'is_paginated': is_paginated,
    }
    return render(
        request,
        'users/profile.html',
        context=context
    )
