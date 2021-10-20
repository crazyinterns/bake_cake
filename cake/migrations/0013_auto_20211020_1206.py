# Generated by Django 3.2.8 on 2021-10-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0012_auto_20211020_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='berry',
        ),
        migrations.AddField(
            model_name='order',
            name='berry',
            field=models.ManyToManyField(blank=True, to='cake.Berry', verbose_name='ягода'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='decoration',
        ),
        migrations.AddField(
            model_name='order',
            name='decoration',
            field=models.ManyToManyField(blank=True, to='cake.Decoration', verbose_name='декорация'),
        ),
    ]
