from django.contrib import admin

from .models import Organisation, OrgCustomer
# Register your models here.

admin.site.register(Organisation)
admin.site.register(OrgCustomer)