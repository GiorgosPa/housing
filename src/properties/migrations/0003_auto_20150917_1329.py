# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20150917_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='openhousedate',
            field=models.DateField(),
        ),
    ]
