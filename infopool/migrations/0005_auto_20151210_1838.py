# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infopool', '0004_auto_20151210_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diasrecorrido',
            old_name='dia_recorrido',
            new_name='recorrido',
        ),
    ]
