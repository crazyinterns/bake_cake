from cake.models import Order, CakeForm, Layer, Topping, Berry, Decoration
from users.models import CustomUser
from django.db.models import Count, Case, When, Value, CharField


def get_stats():
    # users stats
    customers = Order.objects.values('customer') \
        .aggregate(Count('customer', distinct=True))
    all_users = CustomUser.objects.filter(is_staff=False).count()

    # orders_stats
    choices = Order._meta.get_field('status').flatchoices
    whens = [When(status=k, then=Value(v)) for k, v in choices]

    orders_by_status = (
        Order.objects
        .annotate(get_status_display=Case(*whens, output_field=CharField()))
        .values('get_status_display')
        .annotate(count=Count('status'))
        .order_by()
    )

    total_orders_count = 0
    for order in orders_by_status:
        total_orders_count += order['count']

    # components stats
    # forms
    orders_count_by_forms = {}
    forms = CakeForm.objects.all().values('id', 'name')
    orders_count_by_forms_ids = Order.objects.all().values('form') \
        .annotate(total=Count('form')).order_by('total')
    for ord_form in orders_count_by_forms_ids:
        for form in forms:
            if ord_form['form'] == form['id']:
                orders_count_by_forms[form['name']] = ord_form['total']

    # layers
    orders_count_by_layers = {}
    layers = Layer.objects.all().values('id', 'num')
    orders_count_by_layers_ids = Order.objects.all().values('layer') \
        .annotate(total=Count('layer')).order_by('total')
    for ord_layer in orders_count_by_layers_ids:
        for layer in layers:
            if ord_layer['layer'] == layer['id']:
                orders_count_by_layers[layer['num']] = ord_layer['total']

    # toppings
    toppings_by_orders = {}
    for topping in Topping.objects.all().annotate(orders_count=Count('toppings_orders')):
        toppings_by_orders[topping.name] = topping.orders_count

    # berry
    berries_by_orders = {}
    for berry in Berry.objects.all().annotate(orders_count=Count('berries_orders')):
        berries_by_orders[berry.name] = berry.orders_count

    # decoration
    decors_by_orders = {}
    for decor in Decoration.objects.all().annotate(orders_count=Count('decors_orders')):
        decors_by_orders[decor.name] = decor.orders_count

    context = {
        'customers': customers['customer__count'],
        'all_users': all_users,
        'orders_by_status': orders_by_status,
        'total_orders_count': total_orders_count,
        'orders_by_forms': orders_count_by_forms,
        'orders_by_layers': orders_count_by_layers,
        'toppings_by_orders': toppings_by_orders,
        'berries_by_orders': berries_by_orders,
        'decors_by_orders': decors_by_orders,
    }

    return context
