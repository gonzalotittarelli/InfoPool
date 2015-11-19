# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('infopool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilViajero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(max_length=256, null=True, upload_to=b'')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='administrador',
            name='persona_ptr',
        ),
        migrations.RemoveField(
            model_name='viajero',
            name='persona_ptr',
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='viajero_calificado',
            field=models.ForeignKey(related_name='viajero_calificado', to='infopool.PerfilViajero'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='viajero_calificador',
            field=models.ForeignKey(related_name='viajero_calificador', to='infopool.PerfilViajero'),
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='denunciado',
            field=models.ForeignKey(related_name='denunciado', to='infopool.PerfilViajero'),
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='denunciante',
            field=models.ForeignKey(related_name='denunciante', to='infopool.PerfilViajero'),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='destinatario',
            field=models.ForeignKey(related_name='destinatario', to='infopool.PerfilViajero'),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='remitente',
            field=models.ForeignKey(related_name='remitente', to='infopool.PerfilViajero'),
        ),
        migrations.AlterField(
            model_name='peticion',
            name='participante',
            field=models.ForeignKey(related_name='participante', to='infopool.PerfilViajero'),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='conductor',
            field=models.ForeignKey(related_name='conductor', to='infopool.PerfilViajero'),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='pasajeros',
            field=models.ManyToManyField(related_name='pasajeros', to='infopool.PerfilViajero'),
        ),
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.DeleteModel(
            name='Viajero',
        ),
    ]
