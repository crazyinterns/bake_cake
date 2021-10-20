# Generated by Django 3.2.8 on 2021-10-20 08:51

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_alter_layer_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='num',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, '1 слой'), (2, '2 слоя'), (3, '3 слоя')], max_length=5, verbose_name='количество слоёв'),
        ),
    ]
