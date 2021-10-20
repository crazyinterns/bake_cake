from django.contrib import admin
from cake.models import OrderItem, Order, CakeForm, Layer, Promo, Component, ComponentCategory


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'price',
    ]
    list_display_links = [
        'name',
    ]
    list_filter = [
        'category',
    ]
    search_fields = [
        'name',
        'category__name',
    ]


@admin.register(ComponentCategory)
class ComponentCategory(admin.ModelAdmin):
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
    search_fields = [
        
    ]
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
        'component',
    ]