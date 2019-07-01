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


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Categories._meta.fields]


@admin.register(models.Campaigns)
class CampaignsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Campaigns._meta.fields]


@admin.register(models.IpAddresses)
class IpAddressesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.IpAddresses._meta.fields]



@admin.register(models.AssetDownloads)
class AssetDownloadsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.AssetDownloads._meta.fields]
    raw_id_fields = ['asset', 'ip', 'lead', 'email']


@admin.register(models.Assets)
class AssetsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Assets._meta.fields]
    raw_id_fields = ['category', ]


@admin.register(models.AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.AuditLog._meta.fields]


@admin.register(models.LeadDevices)
class LeadDevicesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.LeadDevices._meta.fields]
    list_filter = ['device', 'device_os_name', 'device_os_shortname', 'device_os_platform']


@admin.register(models.LeadEventLog)
class LeadEventLogAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.LeadEventLog._meta.fields]
    raw_id_fields = ['lead', ]
    list_filter = ['action', 'bundle', 'object']


@admin.register(models.Webhooks)
class WebhooksAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Webhooks._meta.fields]
