# Generated by Django 3.2.8 on 2021-10-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0019_auto_20211022_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='promocode',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='промокод'),
        ),
    ]
