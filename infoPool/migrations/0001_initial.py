# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('clave', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'P', max_length=2, choices=[(b'P', b'Pendiente'), (b'A', b'Aceptado'), (b'R', b'Rechazado')])),
            ],
        ),
        migrations.CreateModel(
            name='Recorrido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condicion', models.CharField(max_length=2, choices=[(b'C', b'Conductor'), (b'P', b'Pasajero'), (b'A', b'Ambos')])),
                ('tipo', models.CharField(max_length=3, choices=[(b'D', b'Diario'), (b'PE', b'Periodico'), (b'PU', b'Puntual')])),
                ('fecha_fin', models.DateField(null=True)),
                ('origen_latitud', models.TextField(max_length=200)),
                ('origen_longitud', models.TextField(max_length=200)),
                ('destino_latitud', models.TextField(max_length=200)),
                ('destino_longitud', models.TextField(max_length=200)),
                ('asientos_disponibles', models.IntegerField(default=1)),
                ('evento', models.ForeignKey(to='infoPool.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='infoPool.Persona')),
            ],
            bases=('infoPool.persona',),
        ),
        migrations.CreateModel(
            name='Viajero',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='infoPool.Persona')),
                ('nombres', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=200)),
            ],
            bases=('infoPool.persona',),
        ),
        migrations.AddField(
            model_name='propuesta',
            name='recorrido',
            field=models.ForeignKey(to='infoPool.Recorrido'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='recorrido',
            field=models.ForeignKey(to='infoPool.Recorrido'),
        ),
        migrations.AddField(
            model_name='recorrido',
            name='conductor',
            field=models.ForeignKey(related_name='conductor', to='infoPool.Viajero'),
        ),
        migrations.AddField(
            model_name='recorrido',
            name='pasajeros',
            field=models.ManyToManyField(to='infoPool.Viajero'),
        ),
        migrations.AddField(
            model_name='propuesta',
            name='participante',
            field=models.ForeignKey(related_name='participante', to='infoPool.Viajero'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='autor',
            field=models.ForeignKey(related_name='autor', to='infoPool.Viajero'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='remitente',
            field=models.ForeignKey(related_name='remitente', to='infoPool.Viajero'),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='denunciado',
            field=models.ForeignKey(related_name='denunciado', to='infoPool.Viajero'),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='denunciante',
            field=models.ForeignKey(related_name='denunciante', to='infoPool.Viajero'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(related_name='autor_comentario', to='infoPool.Viajero'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='viajero',
            field=models.ForeignKey(to='infoPool.Viajero'),
        ),
    ]
