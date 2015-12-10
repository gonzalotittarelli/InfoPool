# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infopool', '0003_diasrecorrido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diasrecorrido',
            old_name='recorrido',
            new_name='dia_recorrido',
        ),
    ]
