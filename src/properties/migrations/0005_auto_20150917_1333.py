# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20150917_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='technicalprice',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
