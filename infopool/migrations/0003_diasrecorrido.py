# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infopool', '0002_auto_20151119_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiasRecorrido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.CharField(max_length=5, choices=[(b'l', b'lunes'), (b'mar', b'martes'), (b'mier', b'miercoles'), (b'j', b'jueves'), (b'v', b'viernes')])),
                ('recorrido', models.ForeignKey(to='infopool.Recorrido')),
            ],
        ),
    ]
