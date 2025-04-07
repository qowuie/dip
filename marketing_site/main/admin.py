from django.contrib import admin

from .models import ServiceCategory, Service

# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceCategory)
