from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('order_cake/', views.order_cake, name='order-cake')
]