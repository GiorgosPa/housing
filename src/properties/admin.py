from django.contrib import admin

from .models import Property, Broker, Graph


class PropertyAdmin(admin.ModelAdmin):
    class Meta:
        model = Property


admin.site.register(Property, PropertyAdmin)


class BrokerAdmin(admin.ModelAdmin):
    class Meta:
        model = Broker


admin.site.register(Broker, BrokerAdmin)


class GraphAdmin(admin.ModelAdmin):
    class Meta:
        model = Graph


admin.site.register(Graph, GraphAdmin)
