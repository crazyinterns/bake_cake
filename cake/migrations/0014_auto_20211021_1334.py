# Generated by Django 3.2.8 on 2021-10-21 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0013_auto_20211020_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='cake.cakeform', verbose_name='форма торта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='layer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='cake.layer', verbose_name='количество слоёв'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('NEW', 'Заявка обрабатывается'), ('PREPARING_CAKE', 'Готовим ваш торт'), ('ON_THE_WAY', 'Торт в пути'), ('DELIVERED', 'Торт у вас'), ('CANCELED', 'Отменён')], db_index=True, default='NEW', max_length=20, verbose_name='Статус'),
        ),
    ]