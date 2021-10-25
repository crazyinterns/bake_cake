from django.contrib import admin

from import_export import resources, widgets
from import_export.admin import ImportExportActionModelAdmin
from import_export.fields import Field

from cake.models import Order, CakeForm, Layer, Topping, Berry,\
    Decoration, Promo
from cake.forms import OrderForm
from cake.widgets import choices_widget
from users.models import CustomUser


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
    customer = Field(
        column_name='Пользователь',
        attribute='customer',
        widget=widgets.ForeignKeyWidget(CustomUser, 'get_full_name')
    )
    layer = Field(column_name='Уровень', attribute='layer')
    form = Field(column_name='Форма', attribute='form')
    topping = Field(column_name='Топпинг', attribute='topping')
    berry = Field(column_name='Ягода', attribute='berry')
    decoration = Field(column_name='Декорация')
    status = Field(
        widget=choices_widget.ChoicesWidget(Order.STATUS_CHOICES),
        column_name='Статус',
        attribute='status',
    )
    comment = Field(column_name='Комментарий', attribute='comment')
    writing = Field(column_name='Надпись', attribute='writing')
    created_at = Field(column_name='Заказ создан', attribute='created_at')
    delivery_at = Field(column_name='Заказ доставлен', attribute='delivery_at')

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

    def dehydrate_form(self, order):
        return '{0}'.format(order.form.name)

    def dehydrate_topping(self, order):
        toppings_list = [topping.name for topping in order.topping.all()]
        toppings = ', '.join(toppings_list)

        return '{0}'.format(toppings)

    def dehydrate_berry(self, order):
        berries_list = [berry.name for berry in order.berry.all()]
        berries = ', '.join(berries_list)

        return '{0}'.format(berries)

    def dehydrate_decoration(self, order):
        decorations_list = [
            decoration.name
            for decoration in order.decoration.all()
        ]
        decorations = ', '.join(decorations_list)

        return '{0}'.format(decorations)


@admin.register(Order)
class OrderAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    form = OrderForm
    resource_class = OrderResource

    list_display = [
        'id',
        'customer',
        'status',
        'comment',
    ]
    list_filter = [
        'status',
    ]

    list_editable = ['status']


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'discont_percent', 'active',
    ]
