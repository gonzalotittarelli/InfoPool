# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoPool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='valor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='descripcion',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensaje',
            name='asunto',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensaje',
            name='cuerpo',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='destino_latitud',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='destino_longitud',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='origen_latitud',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='origen_longitud',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='viajero',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='viajero',
            name='nombres',
            field=models.CharField(max_length=200),
        ),
    ]
