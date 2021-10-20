from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.forms import ModelForm
from cake.models import OrderItem, Order, CakeForm, Layer, Promo, Topping, Berry, Decoration


@admin.register(Topping)
class Topping(admin.ModelAdmin):
    pass

@admin.register(Decoration)
class Decoration(admin.ModelAdmin):
    pass

@admin.register(Berry)
class Berry(admin.ModelAdmin):
    pass

@admin.register(CakeForm)
class CakeForm(admin.ModelAdmin):
    pass


@admin.register(Layer)
class Layer(admin.ModelAdmin):
    pass


class OrderAdminForm(ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {
            'topping': CheckboxSelectMultiple,
            'decoration': CheckboxSelectMultiple,
            'berry': CheckboxSelectMultiple,
        }


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
        'id',
        'customer',
        'status',
        'comment'
    ]
    list_filter = [
        'status',
    ]

    list_editable = ['status', ]
