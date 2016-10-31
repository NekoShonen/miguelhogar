# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miguelHogarSyte', '0004_remove_producto_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seleccionados',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('productos', models.ManyToManyField(to='miguelHogarSyte.Producto')),
            ],
        ),
    ]
