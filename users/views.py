from django.shortcuts import render

from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import logout, authenticate, login
from users.forms import CustomUserCreationForm
from django.shortcuts import reverse
from django.shortcuts import render, get_object_or_404
from users.models import CustomUser
from users.forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf import settings


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


def serialize_order(order):

    patterns = {'форма': [],  'слоев': [], 'ягоды': [], 'декор': [], 'топпинг': [],}
    order_price = 0

    for berry in order.berry.all():
        order_price += berry.price
        patterns['ягоды'].append(berry.name)

    for dec in order.decoration.all():
        patterns['декор'].append(dec.name)
        order_price += dec.price

    for top in order.topping.all():
        order_price += top.price
        patterns['топпинг'].append(top.name)

    order_price += order.layer.price
    order_price += order.form.price
    order.price = order_price

    patterns['слоев'].append(order.layer.num)
    patterns['форма'].append(order.form.name)
    order.patterns = patterns

    return {
        'id': order.id,
        'status': order.get_status_display(),
        'price': order.price,
        'fullname': f'{order.customer.first_name} \
            {order.customer.last_name}',
        'comment': order.comment,
        'patterns': order.patterns,
    }


@login_required(login_url='/users/login/')
def profile(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    orders = list(user.orders.all().select_related('layer','form') \
        .prefetch_related('berry','decoration','topping'))

    paginator = Paginator(orders, settings.ITEMS_PER_PAGE)

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
        'page_obj': [
            serialize_order(order) for order in page
        ],
        'user_form': form,
        'is_paginated': is_paginated,
    }
    return render(
        request,
        'users/profile.html',
        context=context
    )
