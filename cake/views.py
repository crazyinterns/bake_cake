from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from cake.models import Order
from django.shortcuts import reverse


def index(request):
    return render(request, 'index.html')

def order_cake(request):
    return render(request, 'order_custom_cake.html')


@login_required(login_url='/users/login/')
def cancel_order(request, pk):
    if request.method == 'POST':
        user = request.user
        order = get_object_or_404(Order, id=pk)
        order.status = 'CANCELLED'
        order.save()
        return HttpResponseRedirect(reverse('profile', args=[user.id]))
