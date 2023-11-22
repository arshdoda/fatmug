from django.contrib import admin
from apps.vendors.models import *

admin.site.register(Vendor)
admin.site.register(HistoricPerformance)