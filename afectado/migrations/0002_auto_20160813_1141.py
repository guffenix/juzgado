# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afectado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afectado',
            name='id',
        ),
        migrations.AlterField(
            model_name='afectado',
            name='id_afectado',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
