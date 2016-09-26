# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miguelHogarSyte', '0002_auto_20160926_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='descuento',
            name='productos',
            field=models.ManyToManyField(to='miguelHogarSyte.Producto'),
        ),
    ]
