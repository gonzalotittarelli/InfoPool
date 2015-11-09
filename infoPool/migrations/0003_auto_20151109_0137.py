# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('infoPool', '0002_auto_20151109_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='texto',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 11, 9, 1, 36, 50, 552736, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='lugar',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recorrido',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2015, 11, 9, 1, 37, 12, 218562, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recorrido',
            name='fecha_publicacion',
            field=models.DateField(default=datetime.datetime(2015, 11, 9, 1, 37, 17, 308925, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recorrido',
            name='hora_llegada',
            field=models.DateTimeField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recorrido',
            name='hora_partida',
            field=models.DateTimeField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viajero',
            name='bloqueado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='viajero',
            name='foto',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viajero',
            name='telefono',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='asunto',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='cuerpo',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='destino_latitud',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='destino_longitud',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='origen_latitud',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='origen_longitud',
            field=models.TextField(max_length=200),
        ),
    ]
