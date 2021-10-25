# Generated by Django 3.2.8 on 2021-10-25 04:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0022_auto_20211022_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='fixed_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='berry',
            field=models.ManyToManyField(blank=True, related_name='berries_orders', to='cake.Berry', verbose_name='ягода'),
        ),
        migrations.AlterField(
            model_name='order',
            name='decoration',
            field=models.ManyToManyField(blank=True, related_name='decors_orders', to='cake.Decoration', verbose_name='декорация'),
        ),
        migrations.AlterField(
            model_name='order',
            name='topping',
            field=models.ManyToManyField(blank=True, related_name='toppings_orders', to='cake.Topping', verbose_name='топпинг'),
        ),
    ]
