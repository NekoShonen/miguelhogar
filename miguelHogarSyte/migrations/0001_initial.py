# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('codigoDeBarras', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=20)),
                ('rubro', models.CharField(max_length=200)),
                ('marca', models.ForeignKey(to='miguelHogarSyte.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('celular', models.IntegerField()),
                ('marcaDistribuye', models.ForeignKey(to='miguelHogarSyte.Marca')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(to='miguelHogarSyte.Proveedor'),
        ),
    ]
