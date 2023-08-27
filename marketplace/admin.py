from django.contrib import admin

from marketplace.models import Vendor, Order, Trip, DelayReport 

admin.site.register(Vendor)
admin.site.register(Order)
admin.site.register(Trip)
admin.site.register(DelayReport)
