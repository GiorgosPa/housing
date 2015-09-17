# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20150917_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='openhousedate',
            field=models.IntegerField(),
        ),
    ]
