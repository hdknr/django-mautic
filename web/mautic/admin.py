from django.contrib import admin
from . import models

# Contacts (Leads)
# https://www.mautic.org/docs/jp/contacts/index.html 
@admin.register(models.Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Leads._meta.fields]


# Segment(LeadList)
@admin.register(models.LeadLists)
class LeadListsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.LeadLists._meta.fields]


# Segmented Lead(LeadListsLeads)
@admin.register(models.LeadListsLeads)
class LeadListsLeadsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.LeadListsLeads._meta.fields]
    raw_id_fields = ['lead', 'leadlist', ]