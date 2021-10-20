from django.contrib import admin
from django.forms import CheckboxSelectMultiple
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


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
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
    inlines = [
            OrderItemInline
        ]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = [
        
    ]
    list_display = [
        'order',
    ]