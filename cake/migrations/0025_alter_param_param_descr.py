# Generated by Django 3.2.8 on 2021-10-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0024_auto_20211025_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='param',
            name='param_descr',
            field=models.CharField(max_length=100, verbose_name='описание параметра'),
        ),
    ]
