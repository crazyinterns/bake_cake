from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.forms import CheckboxSelectMultiple
from django.forms import ModelForm

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from cake.models import Order, CakeForm, Layer, Topping, Berry, Decoration


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
class OrderAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    form = OrderAdminForm
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
