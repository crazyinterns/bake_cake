
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields import NullBooleanField
from django.utils import timezone
from users.models import CustomUser



class Decoration(models.Model):
    name = models.CharField(
        'название',
        max_length=64,
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    description = models.TextField(
        'описание',
        blank=True,
    )

    class Meta:
        verbose_name = 'декорация'
        verbose_name_plural = 'декорации'

    def __str__(self):
        return '{0} ({1:.0f} руб.)'.format(self.name, self.price)


class Berry(models.Model):
    name = models.CharField(
        'название',
        max_length=64,
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    description = models.TextField(
        'описание',
        blank=True,
    )

    class Meta:
        verbose_name = 'ягода'
        verbose_name_plural = 'ягоды'

    def __str__(self):
        return '{0} ({1:.0f} руб.)'.format(self.name, self.price)


class Topping(models.Model):
    name = models.CharField(
        'название',
        max_length=64,
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    description = models.TextField(
        'описание',
        blank=True,
    )

    class Meta:
        verbose_name = 'топпинг'
        verbose_name_plural = 'топпинги'

    def __str__(self):
        return '{0} ({1:.0f} руб.)'.format(self.name, self.price)


class Layer(models.Model):
    num = models.PositiveSmallIntegerField(
        'количество слоёв',
    )

    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = 'Слой'
        verbose_name_plural = 'Слои'

    def __str__(self):
        return '{0} ({1:.0f} руб.)'.format(self.num, self.price)


class CakeForm(models.Model):
    name = models.CharField(
        'форма',
        max_length=50
    )

    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы торта'

    def __str__(self):
        return'{0} ({1:.0f} руб.)'.format(self.name, self.price)


class Order(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'Заявка обрабатывается'),
        ('PREPARING_CAKE', 'Готовим ваш торт'),
        ('ON_THE_WAY', 'Торт в пути'),
        ('DELIVERED', 'Торт у вас'),
        ('CANCELLED', 'Отменён'),
    ]

    layer = models.ForeignKey(
        Layer,
        verbose_name='количество слоёв',
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )

    form = models.ForeignKey(
        CakeForm,
        verbose_name='форма торта',
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )

    topping = models.ManyToManyField(
        Topping,
        verbose_name='топпинг',
        blank=True,
        related_name='toppings_orders'
    )

    berry = models.ManyToManyField(
        Berry,
        verbose_name='ягода',
        blank=True,
        related_name='berries_orders'
    )

    decoration = models.ManyToManyField(
        Decoration,
        verbose_name='декорация',
        blank=True,
        related_name='decors_orders'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NEW',
        verbose_name='Статус',
        db_index=True
    )
    
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True
    )

    writing = models.TextField(
        verbose_name='Надпись на торте',
        blank=True
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата регистрации',
        db_index=True
    )

    delivery_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='когда доставить',
        db_index=True
    )
    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='заказчик',
        related_name='orders'
    )
    promocode = models.CharField(
        'промокод',
        max_length=15,
        null=True,
        blank=True,
        default=''
    )

    address = models.CharField(
        'адрес',
        max_length=128,
        blank=True,
        null=True
    )
    fixed_price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0
    )

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f"{self.id} {self.customer.first_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='заказ'
    )

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return f"\
            {self.component.name} \
            {self.order.customer.first_name} \
            {self.order.customer.last_name}"


class Promo(models.Model):
    name = models.CharField(max_length=15, verbose_name='промокод')
    discont_percent = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name='Скидка %'
    )
    active = models.BooleanField(default=False, verbose_name='активен')
    
    class Meta:
        verbose_name = 'Промокод',
        verbose_name_plural = 'Промокоды'