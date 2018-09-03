from django.contrib import admin
from apps.vehicle.models import Vehicle, Type, Brand, Model

admin.site.register(Vehicle)
admin.site.register(Type)
admin.site.register(Brand)
admin.site.register(Model)
