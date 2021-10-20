from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def order_cake(request):
    return render(request, 'order_custom_cake.html')