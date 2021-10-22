from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from cake.models import Order
from django.shortcuts import reverse
from .forms import OrderForm


def index(request):
    return render(request, 'index.html')

@login_required(login_url='/users/login/')
def order_cake(request):
    submitted = False
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/order_cake?submitted=True')
    else:
        form = OrderForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'order_custom_cake.html', {'form': form, 'submitted': submitted})


@login_required(login_url='/users/login/')
def cancel_order(request, pk):
    if request.method == 'POST':
        user = request.user
        order = get_object_or_404(Order, id=pk)
        order.status = 'CANCELLED'
        order.save()
        return HttpResponseRedirect(reverse('profile', args=[user.id]))
