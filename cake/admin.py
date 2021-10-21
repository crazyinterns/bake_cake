from django.contrib import admin
from django.utils.translation import ngettext

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from cake.models import Order, CakeForm, Layer, Topping, Berry, Decoration
from cake.forms import OrderForm

@admin.register(Topping)
class Topping(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price',
    ]

@admin.register(Decoration)
class Decoration(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price',
    ]

@admin.register(Berry)
class Berry(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price',
    ]

@admin.register(CakeForm)
class CakeFormAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price',
    ]


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'num', 'price',
    ]


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'layer',
            'form',
            'topping',
            'berry',
            'decoration',
            'status',
            'comment',
            'writing',
            'created_at',
            'delivery_at',
        )

        export_order = (
            'id',
            'customer',
            'layer',
            'form',
            'topping',
            'berry',
            'decoration',
            'status',
            'comment',
            'writing',
            'created_at',
            'delivery_at',
        )


@admin.register(Order)
class OrderAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    form = OrderForm
    resource_class = OrderResource

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
