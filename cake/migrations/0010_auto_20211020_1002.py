# Generated by Django 3.2.8 on 2021-10-20 10:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0009_alter_order_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'ягода',
                'verbose_name_plural': 'ягоды',
            },
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'декорация',
                'verbose_name_plural': 'декорации',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='berry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cake.berry', verbose_name='ягода'),
        ),
        migrations.AddField(
            model_name='order',
            name='decoration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cake.decoration', verbose_name='декорация'),
        ),
    ]
