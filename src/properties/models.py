from django.db import models


class Broker(models.Model):
    logo = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    casenumber = models.CharField(max_length=20)
    presentationurl = models.CharField(max_length=200)


class Property(models.Model):
    brutto = models.CharField(max_length=10)
    ownerexpenses = models.CharField(max_length=10)
    openhousedate = models.IntegerField(null=True)
    photo = models.CharField(max_length=200)
    energy = models.CharField(max_length=5)
    price = models.CharField(max_length=20)
    type_raw = models.CharField(max_length=50)
    rooms = models.IntegerField()
    year = models.IntegerField()
    salesperiod = models.IntegerField()
    agentchain = models.CharField(max_length=200)
    usageexpenses = models.CharField(max_length=10)
    floor = models.IntegerField()
    directlink = models.CharField(max_length=200)
    lot = models.IntegerField()
    latitude = models.DecimalField(max_digits=16, decimal_places=10)
    propertycharges = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    clicks = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    salesperiodtotal = models.IntegerField()
    bigphoto = models.CharField(max_length=200)
    floors = models.IntegerField()
    basement = models.IntegerField()
    area = models.IntegerField()
    price = models.CharField(max_length=20)
    netto = models.CharField(max_length=10)
    payment = models.CharField(max_length=10)
    technicalprice = models.CharField(max_length=20, null=True)
    pricedevelopment = models.CharField(max_length=20)
    sqftprice = models.CharField(max_length=10)
    openhouseduration = models.IntegerField(null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=10)
    link = models.CharField(max_length=200)
    broker = models.ForeignKey(Broker)


class Graph(models.Model):
    graph = models.CharField(max_length=200)
    property = models.ForeignKey(Property)
