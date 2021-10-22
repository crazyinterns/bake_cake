from django.urls import path
from django.views.i18n import JavaScriptCatalog
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('order_cake/', views.order_cake, name='order-cake'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('cancel_order/<int:pk>', views.cancel_order, name='cancel_order'),
]