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
                ('fecha', models.DateField(auto_now_add=True)),
                ('tipo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('latitud', models.DecimalField(max_digits=10, decimal_places=6)),
                ('longitud', models.DecimalField(max_digits=10, decimal_places=6)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asunto', models.CharField(max_length=300)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=200)),
                ('clave', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Peticion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('estado', models.CharField(default=b'p', max_length=2, choices=[(b'p', b'pendiente'), (b'a', b'aceptada'), (b'r', b'rechazada')])),
            ],
        ),
        migrations.CreateModel(
            name='Recorrido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=3, choices=[(b'd', b'diario'), (b'pe', b'periodico'), (b'pu', b'puntual')])),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(null=True, blank=True)),
                ('hora_partida', models.TimeField()),
                ('hora_regreso', models.TimeField(null=True, blank=True)),
                ('direccion_destino', models.CharField(max_length=200)),
                ('direccion_origen', models.CharField(max_length=200)),
                ('asientos_disponibles', models.IntegerField(default=1)),
                ('ruta', models.CharField(max_length=300)),
                ('evento', models.ForeignKey(blank=True, to='infopool.Evento', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='infopool.Persona')),
            ],
            bases=('infopool.persona',),
        ),
        migrations.CreateModel(
            name='Viajero',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='infopool.Persona')),
                ('nombres', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('foto', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('bloqueado', models.BooleanField(default=False)),
            ],
            bases=('infopool.persona',),
        ),
        migrations.AddField(
            model_name='peticion',
            name='recorrido',
            field=models.ForeignKey(to='infopool.Recorrido'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='recorrido_calificado',
            field=models.ForeignKey(to='infopool.Recorrido'),
        ),
        migrations.AddField(
            model_name='recorrido',
            name='conductor',
            field=models.ForeignKey(related_name='conductor', to='infopool.Viajero'),
        ),
        migrations.AddField(
            model_name='recorrido',
            name='pasajeros',
            field=models.ManyToManyField(related_name='pasajeros', to='infopool.Viajero'),
        ),
        migrations.AddField(
            model_name='peticion',
            name='participante',
            field=models.ForeignKey(related_name='participante', to='infopool.Viajero'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='destinatario',
            field=models.ForeignKey(related_name='destinatario', to='infopool.Viajero'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='remitente',
            field=models.ForeignKey(related_name='remitente', to='infopool.Viajero'),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='denunciado',
            field=models.ForeignKey(related_name='denunciado', to='infopool.Viajero'),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='denunciante',
            field=models.ForeignKey(related_name='denunciante', to='infopool.Viajero'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='viajero_calificado',
            field=models.ForeignKey(related_name='viajero_calificado', to='infopool.Viajero'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='viajero_calificador',
            field=models.ForeignKey(related_name='viajero_calificador', to='infopool.Viajero'),
        ),
    ]
