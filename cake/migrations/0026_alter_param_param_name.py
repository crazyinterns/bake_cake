# Generated by Django 3.2.8 on 2021-10-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0025_alter_param_param_descr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='param',
            name='param_name',
            field=models.CharField(default=1, max_length=30, unique=True, verbose_name='параметр'),
            preserve_default=False,
        ),
    ]