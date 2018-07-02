from django.contrib import admin
from . import models

# Contacts (Leads)
# https://www.mautic.org/docs/jp/contacts/index.html 


@admin.register(models.Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Leads._meta.fields]