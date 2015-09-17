# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('casenumber', models.CharField(max_length=20)),
                ('presentationurl', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('graph', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agentchain', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('directlink', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('type_raw', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=200)),
                ('bigphoto', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('clicks', models.IntegerField(default=0)),
                ('rooms', models.IntegerField()),
                ('floors', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('lot', models.IntegerField()),
                ('basement', models.IntegerField()),
                ('energy', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('area', models.IntegerField()),
                ('price', models.CharField(max_length=20)),
                ('bruto', models.CharField(max_length=5)),
                ('netto', models.CharField(max_length=5)),
                ('payment', models.CharField(max_length=5)),
                ('technicalprice', models.CharField(max_length=20)),
                ('pricedevelopment', models.CharField(max_length=20)),
                ('salesperiodtotal', models.IntegerField()),
                ('salesperiod', models.IntegerField()),
                ('propertycharges', models.CharField(max_length=10)),
                ('usageexpenses', models.CharField(max_length=10)),
                ('ownerexpenses', models.CharField(max_length=10)),
                ('sqftprice', models.CharField(max_length=10)),
                ('openhousedate', models.DateTimeField()),
                ('openhouseduration', models.IntegerField()),
                ('latitude', models.DecimalField(max_digits=16, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=16, decimal_places=10)),
                ('broker', models.ForeignKey(to='properties.Broker')),
            ],
        ),
        migrations.AddField(
            model_name='graph',
            name='property',
            field=models.ForeignKey(to='properties.Property'),
        ),
    ]
