from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from cake.models import Order
from .forms import OrderForm
from users.views import serialize_order, get_order_price


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/users/login/')
def order_cake(request):
    user = request.user
    submitted = False
    if request.method == 'POST':

        form = OrderForm(request.POST)
        if form.is_valid():

            cleaned_data = form.cleaned_data

            order = Order(
                layer=cleaned_data['layer'],
                form=cleaned_data['form'],
                promocode=cleaned_data['promocode'],
                customer=user,
                address=cleaned_data['address'],
                delivery_at=cleaned_data['delivery_at'],
                comment=cleaned_data['comment'],
                writing=cleaned_data['writing'],
                fixed_price=0,
            )
      
            order.save()
            order.berry.set(cleaned_data['berry']),
            order.decoration.set(cleaned_data['decoration'])
            order.topping.set(cleaned_data['topping'])

            order.fixed_price = get_order_price(order)

            order.save()

            return HttpResponseRedirect('/order_cake?submitted=True')
    else:
        form = OrderForm
        if 'submitted' in request.GET:
            submitted = True

    orders = list(
        user.orders.exclude(status='CANCELLED')\
        .select_related('layer', 'form')\
        .prefetch_related('berry', 'decoration', 'topping')\
        .order_by('-id'),
    )

    context = {
        'form': form,
        'submitted': submitted,
        'page_obj': [serialize_order(order) for order in orders],
    }

    return render(request, 'order_custom_cake.html', context=context)


@login_required(login_url='/users/login/')
def cancel_order(request, pk):
    if request.method == 'POST':
        user = request.user
        comment = request.POST.get('comment')
        order = get_object_or_404(Order, id=pk)
        order.status = 'CANCELLED'
        order.comment = comment
        order.save()
        return HttpResponseRedirect(reverse('profile', args=[user.id]))
