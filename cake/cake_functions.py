from cake.models import Param
from decimal import Decimal


def get_addittional_prices():
    writing_price = Decimal(0)
    express_delivery_koef = Decimal(1)

    params = Param.objects.filter(
        param_name__in=('WRITING_PRICE', 'EXPRESS_DELIVERY_KOEF')
        )

    for param in params:
        if param.param_name == 'WRITING_PRICE':
            writing_price = Decimal(param.param_value)
        if param.param_name == 'EXPRESS_DELIVERY_KOEF':
            express_delivery_koef = Decimal(param.param_value)

    return writing_price, express_delivery_koef