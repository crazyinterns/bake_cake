from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import OrderForm

def index(request):
    return render(request, 'index.html')

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
