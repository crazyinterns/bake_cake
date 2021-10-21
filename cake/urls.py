from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('order_cake/', views.order_cake, name='order-cake'),
    path('cancel_order/<int:pk>', views.cancel_order, name='cancel_order'),
]