# Generated by Django 3.2.8 on 2021-10-22 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0017_alter_promo_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='адрес'),
        ),
    ]
