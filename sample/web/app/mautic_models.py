# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AssetDownloads(models.Model):
    asset = models.ForeignKey('Assets', models.DO_NOTHING, blank=True, null=True)
    ip = models.ForeignKey('IpAddresses', models.DO_NOTHING)
    lead = models.ForeignKey('Leads', models.DO_NOTHING, blank=True, null=True)
    email = models.ForeignKey('Emails', models.DO_NOTHING, blank=True, null=True)
    date_download = models.DateTimeField()
    code = models.IntegerField()
    referer = models.TextField(blank=True, null=True)
    tracking_id = models.CharField(max_length=255)
    source = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_downloads'


class Assets(models.Model):
    category = models.ForeignKey('Categories', models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    alias = models.CharField(max_length=255)
    storage_location = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    remote_path = models.CharField(max_length=255, blank=True, null=True)
    original_file_name = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    download_count = models.IntegerField()
    unique_download_count = models.IntegerField()
    revision = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    mime = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    disallow = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets'


class AuditLog(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=255)
    bundle = models.CharField(max_length=50)
    object = models.CharField(max_length=50)
    object_id = models.IntegerField()
    action = models.CharField(max_length=50)
    details = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField()
    ip_address = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'audit_log'


class CacheItems(models.Model):
    item_id = models.CharField(primary_key=True, max_length=255)
    item_data = models.TextField()
    item_lifetime = models.PositiveIntegerField(blank=True, null=True)
    item_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_items'


class CampaignEvents(models.Model):
    campaign = models.ForeignKey('Campaigns', models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50)
    event_type = models.CharField(max_length=50)
    event_order = models.IntegerField()
    properties = models.TextField()
    trigger_date = models.DateTimeField(blank=True, null=True)
    trigger_interval = models.IntegerField(blank=True, null=True)
    trigger_interval_unit = models.CharField(max_length=1, blank=True, null=True)
    trigger_mode = models.CharField(max_length=10, blank=True, null=True)
    decision_path = models.CharField(max_length=255, blank=True, null=True)
    temp_id = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_events'


class CampaignFormXref(models.Model):
    campaign = models.ForeignKey('Campaigns', models.DO_NOTHING, primary_key=True)
    form = models.ForeignKey('Forms', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_form_xref'
        unique_together = (('campaign', 'form'),)


class CampaignLeadEventFailedLog(models.Model):
    log = models.ForeignKey('CampaignLeadEventLog', models.DO_NOTHING, primary_key=True)
    date_added = models.DateTimeField()
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_lead_event_failed_log'


class CampaignLeadEventLog(models.Model):
    event = models.ForeignKey(CampaignEvents, models.DO_NOTHING)
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    campaign = models.ForeignKey('Campaigns', models.DO_NOTHING, blank=True, null=True)
    ip = models.ForeignKey('IpAddresses', models.DO_NOTHING, blank=True, null=True)
    rotation = models.IntegerField()
    date_triggered = models.DateTimeField(blank=True, null=True)
    is_scheduled = models.IntegerField()
    trigger_date = models.DateTimeField(blank=True, null=True)
    system_triggered = models.IntegerField()
    metadata = models.TextField(blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_id = models.IntegerField(blank=True, null=True)
    non_action_path_taken = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_lead_event_log'
        unique_together = (('event', 'lead', 'rotation'),)


class CampaignLeadlistXref(models.Model):
    campaign = models.ForeignKey('Campaigns', models.DO_NOTHING, primary_key=True)
    leadlist = models.ForeignKey('LeadLists', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_leadlist_xref'
        unique_together = (('campaign', 'leadlist'),)


class CampaignLeads(models.Model):
    campaign = models.ForeignKey('Campaigns', models.DO_NOTHING, primary_key=True)
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    date_added = models.DateTimeField()
    manually_removed = models.IntegerField()
    manually_added = models.IntegerField()
    date_last_exited = models.DateTimeField(blank=True, null=True)
    rotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'campaign_leads'
        unique_together = (('campaign', 'lead'),)


class Campaigns(models.Model):
    category = models.ForeignKey('Categories', models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    canvas_settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaigns'


class Categories(models.Model):
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    alias = models.CharField(max_length=255)
    color = models.CharField(max_length=7, blank=True, null=True)
    bundle = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categories'


class ChannelUrlTrackables(models.Model):
    redirect = models.ForeignKey('PageRedirects', models.DO_NOTHING, primary_key=True)
    channel_id = models.IntegerField()
    channel = models.CharField(max_length=255)
    hits = models.IntegerField()
    unique_hits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'channel_url_trackables'
        unique_together = (('redirect', 'channel_id'),)


class Companies(models.Model):
    owner = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    social_cache = models.TextField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    companyemail = models.CharField(max_length=255, blank=True, null=True)
    companyaddress1 = models.CharField(max_length=255, blank=True, null=True)
    companyaddress2 = models.CharField(max_length=255, blank=True, null=True)
    companyphone = models.CharField(max_length=255, blank=True, null=True)
    companycity = models.CharField(max_length=255, blank=True, null=True)
    companystate = models.CharField(max_length=255, blank=True, null=True)
    companyzipcode = models.CharField(max_length=255, blank=True, null=True)
    companycountry = models.CharField(max_length=255, blank=True, null=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    companywebsite = models.TextField(blank=True, null=True)
    companyindustry = models.CharField(max_length=255, blank=True, null=True)
    companydescription = models.TextField(blank=True, null=True)
    companynumber_of_employees = models.FloatField(blank=True, null=True)
    companyfax = models.CharField(max_length=255, blank=True, null=True)
    companyannual_revenue = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class CompaniesLeads(models.Model):
    company = models.ForeignKey(Companies, models.DO_NOTHING, primary_key=True)
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    date_added = models.DateTimeField()
    is_primary = models.IntegerField(blank=True, null=True)
    manually_removed = models.IntegerField()
    manually_added = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'companies_leads'
        unique_together = (('company', 'lead'),)


class ContactMergeRecords(models.Model):
    contact = models.ForeignKey('Leads', models.DO_NOTHING)
    date_added = models.DateTimeField()
    merged_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contact_merge_records'


class DynamicContent(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    translation_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    variant_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    sent_count = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=255)
    variant_settings = models.TextField(blank=True, null=True)
    variant_start_date = models.DateTimeField(blank=True, null=True)
    filters = models.TextField(blank=True, null=True)
    is_campaign_based = models.IntegerField()
    slot_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamic_content'


class DynamicContentLeadData(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    dynamic_content = models.ForeignKey(DynamicContent, models.DO_NOTHING, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    slot = models.TextField()

    class Meta:
        managed = False
        db_table = 'dynamic_content_lead_data'


class DynamicContentStats(models.Model):
    dynamic_content = models.ForeignKey(DynamicContent, models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey('Leads', models.DO_NOTHING, blank=True, null=True)
    date_sent = models.DateTimeField()
    source = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    tokens = models.TextField(blank=True, null=True)
    sent_count = models.IntegerField(blank=True, null=True)
    last_sent = models.DateTimeField(blank=True, null=True)
    sent_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamic_content_stats'


class EmailAssetsXref(models.Model):
    email = models.ForeignKey('Emails', models.DO_NOTHING, primary_key=True)
    asset = models.ForeignKey(Assets, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_assets_xref'
        unique_together = (('email', 'asset'),)


class EmailCopies(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    date_created = models.DateTimeField()
    body = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_copies'


class EmailListXref(models.Model):
    email = models.ForeignKey('Emails', models.DO_NOTHING, primary_key=True)
    leadlist = models.ForeignKey('LeadLists', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_list_xref'
        unique_together = (('email', 'leadlist'),)


class EmailStatReplies(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    stat = models.ForeignKey('EmailStats', models.DO_NOTHING)
    date_replied = models.DateTimeField()
    message_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'email_stat_replies'


class EmailStats(models.Model):
    email = models.ForeignKey('Emails', models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey('Leads', models.DO_NOTHING, blank=True, null=True)
    list = models.ForeignKey('LeadLists', models.DO_NOTHING, blank=True, null=True)
    ip = models.ForeignKey('IpAddresses', models.DO_NOTHING, blank=True, null=True)
    copy = models.ForeignKey(EmailCopies, models.DO_NOTHING, blank=True, null=True)
    email_address = models.CharField(max_length=255)
    date_sent = models.DateTimeField()
    is_read = models.IntegerField()
    is_failed = models.IntegerField()
    viewed_in_browser = models.IntegerField()
    date_read = models.DateTimeField(blank=True, null=True)
    tracking_hash = models.CharField(max_length=255, blank=True, null=True)
    retry_count = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    tokens = models.TextField(blank=True, null=True)
    open_count = models.IntegerField(blank=True, null=True)
    last_opened = models.DateTimeField(blank=True, null=True)
    open_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_stats'


class EmailStatsDevices(models.Model):
    device = models.ForeignKey('LeadDevices', models.DO_NOTHING, blank=True, null=True)
    stat = models.ForeignKey(EmailStats, models.DO_NOTHING, blank=True, null=True)
    ip = models.ForeignKey('IpAddresses', models.DO_NOTHING, blank=True, null=True)
    date_opened = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_stats_devices'


class Emails(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    translation_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    variant_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    unsubscribeform = models.ForeignKey('Forms', models.DO_NOTHING, blank=True, null=True)
    preference_center = models.ForeignKey('Pages', models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    from_address = models.CharField(max_length=255, blank=True, null=True)
    from_name = models.CharField(max_length=255, blank=True, null=True)
    reply_to_address = models.CharField(max_length=255, blank=True, null=True)
    bcc_address = models.CharField(max_length=255, blank=True, null=True)
    template = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    utm_tags = models.TextField(blank=True, null=True)
    plain_text = models.TextField(blank=True, null=True)
    custom_html = models.TextField(blank=True, null=True)
    email_type = models.TextField(blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    read_count = models.IntegerField()
    sent_count = models.IntegerField()
    revision = models.IntegerField()
    lang = models.CharField(max_length=255)
    variant_settings = models.TextField(blank=True, null=True)
    variant_start_date = models.DateTimeField(blank=True, null=True)
    dynamic_content = models.TextField(blank=True, null=True)
    variant_sent_count = models.IntegerField()
    variant_read_count = models.IntegerField()
    headers = models.TextField()

    class Meta:
        managed = False
        db_table = 'emails'


class Focus(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    focus_type = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    utm_tags = models.TextField(blank=True, null=True)
    form_id = models.IntegerField(blank=True, null=True)
    cache = models.TextField(blank=True, null=True)
    html_mode = models.CharField(max_length=255, blank=True, null=True)
    editor = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'focus'


class FocusStats(models.Model):
    focus = models.ForeignKey(Focus, models.DO_NOTHING)
    lead = models.ForeignKey('Leads', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=255)
    type_id = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'focus_stats'


class FormActions(models.Model):
    form = models.ForeignKey('Forms', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50)
    action_order = models.IntegerField()
    properties = models.TextField()

    class Meta:
        managed = False
        db_table = 'form_actions'


class FormFields(models.Model):
    form = models.ForeignKey('Forms', models.DO_NOTHING)
    label = models.TextField()
    show_label = models.IntegerField(blank=True, null=True)
    alias = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    is_custom = models.IntegerField()
    custom_parameters = models.TextField(blank=True, null=True)
    default_value = models.TextField(blank=True, null=True)
    is_required = models.IntegerField()
    validation_message = models.TextField(blank=True, null=True)
    help_message = models.TextField(blank=True, null=True)
    field_order = models.IntegerField(blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    label_attr = models.CharField(max_length=255, blank=True, null=True)
    input_attr = models.CharField(max_length=255, blank=True, null=True)
    container_attr = models.CharField(max_length=255, blank=True, null=True)
    lead_field = models.CharField(max_length=255, blank=True, null=True)
    save_result = models.IntegerField(blank=True, null=True)
    is_auto_fill = models.IntegerField(blank=True, null=True)
    show_when_value_exists = models.IntegerField(blank=True, null=True)
    show_after_x_submissions = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_fields'


class FormResults1Fomu(models.Model):
    submission_id = models.IntegerField(primary_key=True)
    form_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'form_results_1_fomu'
        unique_together = (('submission_id', 'form_id'),)


class FormResults2Documentdo(models.Model):
    submission_id = models.IntegerField(primary_key=True)
    form_id = models.IntegerField()
    yu_she_ming = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    dan_dang_zhe_yang_xing = models.TextField(blank=True, null=True)
    dan_dang_zhe_yang_ming = models.TextField(blank=True, null=True)
    dian_hua_fan_hao = models.TextField(blank=True, null=True)
    dou_dao_fu_xian = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_results_2_documentdo'
        unique_together = (('submission_id', 'form_id'),)


class FormResults3Partnerpro(models.Model):
    submission_id = models.IntegerField(primary_key=True)
    form_id = models.IntegerField()
    yu_she_ming = models.TextField(blank=True, null=True)
    yu_sheweb_url = models.TextField(blank=True, null=True)
    go_dan_dang_zhe_yang_ming = models.TextField(blank=True, null=True)
    go_dan_dang_zhe_yang_ming1 = models.TextField(blank=True, null=True)
    go_dan_dang_zhe_yangmerua1 = models.TextField(blank=True, null=True)
    go_dan_dang_zhe_yang_dian = models.TextField(blank=True, null=True)
    zhu_yao_qu_yin_zhi_pin = models.TextField(blank=True, null=True)
    zhu_yao_fan_mai_de_yu = models.TextField(blank=True, null=True)
    xiang_ding_fan_mai_tai_sh = models.TextField(blank=True, null=True)
    dou_dao_fu_xian = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_results_3_partnerpro'
        unique_together = (('submission_id', 'form_id'),)


class FormResults4Recruitcon(models.Model):
    submission_id = models.IntegerField(primary_key=True)
    form_id = models.IntegerField()
    han_zi_xing = models.TextField(blank=True, null=True)
    han_zi_ming = models.TextField(blank=True, null=True)
    kana_xing = models.TextField(blank=True, null=True)
    kana_ming = models.TextField(blank=True, null=True)
    dian_hua_fan_hao = models.TextField(blank=True, null=True)
    meruadoresu = models.TextField(blank=True, null=True)
    xi_wang_zhi_zhong = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_results_4_recruitcon'
        unique_together = (('submission_id', 'form_id'),)


class FormResults5Contact(models.Model):
    submission_id = models.IntegerField(primary_key=True)
    form_id = models.IntegerField()
    yu_she_ming = models.TextField(blank=True, null=True)
    go_dan_dang_zhe_xing = models.TextField(blank=True, null=True)
    go_dan_dang_zhe_ming1 = models.TextField(blank=True, null=True)
    meruadoresu = models.TextField(blank=True, null=True)
    o_wen_hese_jian_ming = models.TextField(blank=True, null=True)
    o_wen_hese_zhong_bie = models.TextField(blank=True, null=True)
    dui_xiang_zhi_pin = models.TextField(blank=True, null=True)
    xiang_ding_tai_shu = models.TextField(blank=True, null=True)
    xian_zai_li_yong_zhongnos = models.TextField(blank=True, null=True)
    zai_fan_dui_xiang_qi_ye_g = models.TextField(blank=True, null=True)
    o_wen_hese_nei_rong = models.TextField(blank=True, null=True)
    dian_hua_fan_hao = models.TextField(blank=True, null=True)
    dou_dao_fu_xian = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_results_5_contact'
        unique_together = (('submission_id', 'form_id'),)


class FormSubmissions(models.Model):
    form = models.ForeignKey('Forms', models.DO_NOTHING)
    ip = models.ForeignKey('IpAddresses', models.DO_NOTHING)
    lead = models.ForeignKey('Leads', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey('Pages', models.DO_NOTHING, blank=True, null=True)
    tracking_id = models.CharField(max_length=255, blank=True, null=True)
    date_submitted = models.DateTimeField()
    referer = models.TextField()

    class Meta:
        managed = False
        db_table = 'form_submissions'


class Forms(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    alias = models.CharField(max_length=255)
    cached_html = models.TextField(blank=True, null=True)
    post_action = models.CharField(max_length=255)
    post_action_property = models.CharField(max_length=255, blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    template = models.CharField(max_length=255, blank=True, null=True)
    in_kiosk_mode = models.IntegerField(blank=True, null=True)
    render_style = models.IntegerField(blank=True, null=True)
    form_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forms'


class Imports(models.Model):
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    dir = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    original_file = models.CharField(max_length=255, blank=True, null=True)
    line_count = models.IntegerField()
    inserted_count = models.IntegerField()
    updated_count = models.IntegerField()
    ignored_count = models.IntegerField()
    priority = models.IntegerField()
    status = models.IntegerField()
    date_started = models.DateTimeField(blank=True, null=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    object = models.CharField(max_length=255)
    properties = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imports'


class IntegrationEntity(models.Model):
    date_added = models.DateTimeField()
    integration = models.CharField(max_length=255, blank=True, null=True)
    integration_entity = models.CharField(max_length=255, blank=True, null=True)
    integration_entity_id = models.CharField(max_length=255, blank=True, null=True)
    internal_entity = models.CharField(max_length=255, blank=True, null=True)
    internal_entity_id = models.IntegerField(blank=True, null=True)
    last_sync_date = models.DateTimeField(blank=True, null=True)
    internal = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integration_entity'


class IpAddresses(models.Model):
    ip_address = models.CharField(max_length=45)
    ip_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_addresses'


class LeadCategories(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    date_added = models.DateTimeField()
    manually_removed = models.IntegerField()
    manually_added = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lead_categories'


class LeadCompaniesChangeLog(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    type = models.TextField()
    event_name = models.CharField(max_length=255)
    action_name = models.CharField(max_length=255)
    company_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lead_companies_change_log'


class LeadDevices(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    date_added = models.DateTimeField()
    client_info = models.TextField(blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    device_os_name = models.CharField(max_length=255, blank=True, null=True)
    device_os_shortname = models.CharField(max_length=255, blank=True, null=True)
    device_os_version = models.CharField(max_length=255, blank=True, null=True)
    device_os_platform = models.CharField(max_length=255, blank=True, null=True)
    device_brand = models.CharField(max_length=255, blank=True, null=True)
    device_model = models.CharField(max_length=255, blank=True, null=True)
    device_fingerprint = models.CharField(max_length=255, blank=True, null=True)
    tracking_id = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead_devices'


class LeadDonotcontact(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING, blank=True, null=True)
    date_added = models.DateTimeField()
    reason = models.SmallIntegerField()
    channel = models.CharField(max_length=255)
    channel_id = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead_donotcontact'


class LeadEventLog(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    bundle = models.CharField(max_length=255, blank=True, null=True)
    object = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()
    properties = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead_event_log'


class LeadFields(models.Model):
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    field_group = models.CharField(max_length=255, blank=True, null=True)
    default_value = models.CharField(max_length=255, blank=True, null=True)
    is_required = models.IntegerField()
    is_fixed = models.IntegerField()
    is_visible = models.IntegerField()
    is_short_visible = models.IntegerField()
    is_listable = models.IntegerField()
    is_publicly_updatable = models.IntegerField()
    is_unique_identifer = models.IntegerField(blank=True, null=True)
    field_order = models.IntegerField(blank=True, null=True)
    object = models.CharField(max_length=255, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead_fields'


class LeadFrequencyrules(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    date_added = models.DateTimeField()
    frequency_number = models.SmallIntegerField(blank=True, null=True)
    frequency_time = models.CharField(max_length=25, blank=True, null=True)
    channel = models.CharField(max_length=255)
    preferred_channel = models.IntegerField()
    pause_from_date = models.DateTimeField(blank=True, null=True)
    pause_to_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead_frequencyrules'


class LeadIpsXref(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING, primary_key=True)
    ip = models.ForeignKey(IpAddresses, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lead_ips_xref'
        unique_together = (('lead', 'ip'),)


class LeadLists(models.Model):
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    alias = models.CharField(max_length=255)
    filters = models.TextField()
    is_global = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lead_lists'


class LeadListsLeads(models.Model):
    leadlist = models.ForeignKey(LeadLists, models.DO_NOTHING, primary_key=True)
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    date_added = models.DateTimeField()
    manually_removed = models.IntegerField()
    manually_added = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lead_lists_leads'
        unique_together = (('leadlist', 'lead'),)


class LeadNotes(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()
    type = models.CharField(max_length=50, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead_notes'


class LeadPointsChangeLog(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    ip = models.ForeignKey(IpAddresses, models.DO_NOTHING)
    type = models.TextField()
    event_name = models.CharField(max_length=255)
    action_name = models.CharField(max_length=255)
    delta = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lead_points_change_log'


class LeadStagesChangeLog(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    stage = models.ForeignKey('Stages', models.DO_NOTHING, blank=True, null=True)
    event_name = models.CharField(max_length=255)
    action_name = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lead_stages_change_log'


class LeadTags(models.Model):
    tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lead_tags'


class LeadTagsXref(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(LeadTags, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lead_tags_xref'
        unique_together = (('lead', 'tag'),)


class LeadUtmtags(models.Model):
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    date_added = models.DateTimeField()
    query = models.TextField(blank=True, null=True)
    referer = models.TextField(blank=True, null=True)
    remote_host = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    utm_campaign = models.CharField(max_length=255, blank=True, null=True)
    utm_content = models.CharField(max_length=255, blank=True, null=True)
    utm_medium = models.CharField(max_length=255, blank=True, null=True)
    utm_source = models.CharField(max_length=255, blank=True, null=True)
    utm_term = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead_utmtags'


class Leads(models.Model):
    owner = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    stage = models.ForeignKey('Stages', models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    points = models.IntegerField()
    last_active = models.DateTimeField(blank=True, null=True)
    internal = models.TextField(blank=True, null=True)
    social_cache = models.TextField(blank=True, null=True)
    date_identified = models.DateTimeField(blank=True, null=True)
    preferred_profile_image = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    preferred_locale = models.CharField(max_length=255, blank=True, null=True)
    attribution_date = models.DateTimeField(blank=True, null=True)
    attribution = models.FloatField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    foursquare = models.CharField(max_length=255, blank=True, null=True)
    googleplus = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    skype = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads'


class MessageChannels(models.Model):
    message = models.ForeignKey('Messages', models.DO_NOTHING)
    channel = models.CharField(max_length=255)
    channel_id = models.IntegerField(blank=True, null=True)
    properties = models.TextField()
    is_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_channels'
        unique_together = (('message', 'channel'),)


class MessageQueue(models.Model):
    event = models.ForeignKey(CampaignEvents, models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey(Leads, models.DO_NOTHING)
    channel = models.CharField(max_length=255)
    channel_id = models.IntegerField()
    priority = models.SmallIntegerField()
    max_attempts = models.SmallIntegerField()
    attempts = models.SmallIntegerField()
    success = models.IntegerField()
    status = models.CharField(max_length=255)
    date_published = models.DateTimeField(blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    last_attempt = models.DateTimeField(blank=True, null=True)
    date_sent = models.DateTimeField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_queue'


class Messages(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class MonitorPostCount(models.Model):
    monitor = models.ForeignKey('Monitoring', models.DO_NOTHING, blank=True, null=True)
    post_date = models.DateField()
    post_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'monitor_post_count'


class Monitoring(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    lists = models.TextField(blank=True, null=True)
    network_type = models.CharField(max_length=255, blank=True, null=True)
    revision = models.IntegerField()
    stats = models.TextField(blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitoring'


class MonitoringLeads(models.Model):
    monitor = models.ForeignKey(Monitoring, models.DO_NOTHING, primary_key=True)
    lead = models.ForeignKey(Leads, models.DO_NOTHING)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'monitoring_leads'
        unique_together = (('monitor', 'lead'),)


class Notifications(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    type = models.CharField(max_length=25, blank=True, null=True)
    header = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    date_added = models.DateTimeField()
    icon_class = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notifications'


class Oauth1AccessTokens(models.Model):
    consumer = models.ForeignKey('Oauth1Consumers', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    token = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    expires_at = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth1_access_tokens'


class Oauth1Consumers(models.Model):
    name = models.CharField(max_length=255)
    consumer_key = models.CharField(max_length=255)
    consumer_secret = models.CharField(max_length=255)
    callback = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oauth1_consumers'


class Oauth1Nonces(models.Model):
    nonce = models.CharField(primary_key=True, max_length=255)
    timestamp = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oauth1_nonces'


class Oauth1RequestTokens(models.Model):
    consumer = models.ForeignKey(Oauth1Consumers, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    token = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    expires_at = models.BigIntegerField()
    verifier = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oauth1_request_tokens'


class Oauth2Accesstokens(models.Model):
    client = models.ForeignKey('Oauth2Clients', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    token = models.CharField(unique=True, max_length=255)
    expires_at = models.BigIntegerField(blank=True, null=True)
    scope = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_accesstokens'


class Oauth2Authcodes(models.Model):
    client = models.ForeignKey('Oauth2Clients', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    token = models.CharField(unique=True, max_length=255)
    expires_at = models.BigIntegerField(blank=True, null=True)
    scope = models.CharField(max_length=255, blank=True, null=True)
    redirect_uri = models.TextField()

    class Meta:
        managed = False
        db_table = 'oauth2_authcodes'


class Oauth2Clients(models.Model):
    name = models.CharField(max_length=255)
    random_id = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    redirect_uris = models.TextField()
    allowed_grant_types = models.TextField()

    class Meta:
        managed = False
        db_table = 'oauth2_clients'


class Oauth2Refreshtokens(models.Model):
    client = models.ForeignKey(Oauth2Clients, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    token = models.CharField(unique=True, max_length=255)
    expires_at = models.BigIntegerField(blank=True, null=True)
    scope = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_refreshtokens'


class Oauth2UserClientXref(models.Model):
    client = models.ForeignKey(Oauth2Clients, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oauth2_user_client_xref'
        unique_together = (('client', 'user'),)


class PageHits(models.Model):
    page = models.ForeignKey('Pages', models.DO_NOTHING, blank=True, null=True)
    redirect = models.ForeignKey('PageRedirects', models.DO_NOTHING, blank=True, null=True)
    email = models.ForeignKey(Emails, models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey(Leads, models.DO_NOTHING, blank=True, null=True)
    ip = models.ForeignKey(IpAddresses, models.DO_NOTHING)
    device = models.ForeignKey(LeadDevices, models.DO_NOTHING, blank=True, null=True)
    date_hit = models.DateTimeField()
    date_left = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    isp = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    code = models.IntegerField()
    referer = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    url_title = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    remote_host = models.CharField(max_length=255, blank=True, null=True)
    page_language = models.CharField(max_length=255, blank=True, null=True)
    browser_languages = models.TextField(blank=True, null=True)
    tracking_id = models.CharField(max_length=255)
    source = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'page_hits'


class PageRedirects(models.Model):
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    redirect_id = models.CharField(max_length=25)
    url = models.TextField()
    hits = models.IntegerField()
    unique_hits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'page_redirects'


class Pages(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    translation_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    variant_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    template = models.CharField(max_length=255, blank=True, null=True)
    custom_html = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    hits = models.IntegerField()
    unique_hits = models.IntegerField()
    variant_hits = models.IntegerField()
    revision = models.IntegerField()
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    redirect_type = models.CharField(max_length=100, blank=True, null=True)
    redirect_url = models.CharField(max_length=2048, blank=True, null=True)
    is_preference_center = models.IntegerField(blank=True, null=True)
    no_index = models.IntegerField(blank=True, null=True)
    lang = models.CharField(max_length=255)
    variant_settings = models.TextField(blank=True, null=True)
    variant_start_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages'


class Permissions(models.Model):
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    bundle = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    bitwise = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permissions'
        unique_together = (('bundle', 'name', 'role'),)


class PluginCitrixEvents(models.Model):
    lead = models.ForeignKey(Leads, models.DO_NOTHING)
    product = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    event_desc = models.CharField(max_length=255, blank=True, null=True)
    event_type = models.CharField(max_length=50)
    event_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'plugin_citrix_events'


class PluginCrmPipedriveOwners(models.Model):
    email = models.CharField(max_length=255)
    owner_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugin_crm_pipedrive_owners'


class PluginIntegrationSettings(models.Model):
    plugin = models.ForeignKey('Plugins', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    is_published = models.IntegerField()
    supported_features = models.TextField(blank=True, null=True)
    api_keys = models.TextField()
    feature_settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugin_integration_settings'


class Plugins(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_missing = models.IntegerField()
    bundle = models.CharField(unique=True, max_length=50)
    version = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugins'


class PointLeadActionLog(models.Model):
    point = models.ForeignKey('Points', models.DO_NOTHING, primary_key=True)
    lead = models.ForeignKey(Leads, models.DO_NOTHING)
    ip = models.ForeignKey(IpAddresses, models.DO_NOTHING, blank=True, null=True)
    date_fired = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'point_lead_action_log'
        unique_together = (('point', 'lead'),)


class PointLeadEventLog(models.Model):
    event = models.ForeignKey('PointTriggerEvents', models.DO_NOTHING, primary_key=True)
    lead = models.ForeignKey(Leads, models.DO_NOTHING)
    ip = models.ForeignKey(IpAddresses, models.DO_NOTHING, blank=True, null=True)
    date_fired = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'point_lead_event_log'
        unique_together = (('event', 'lead'),)


class PointTriggerEvents(models.Model):
    trigger = models.ForeignKey('PointTriggers', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50)
    action_order = models.IntegerField()
    properties = models.TextField()

    class Meta:
        managed = False
        db_table = 'point_trigger_events'


class PointTriggers(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    points = models.IntegerField()
    color = models.CharField(max_length=7)
    trigger_existing_leads = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'point_triggers'


class Points(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    delta = models.IntegerField()
    properties = models.TextField()

    class Meta:
        managed = False
        db_table = 'points'


class PushIds(models.Model):
    lead = models.ForeignKey(Leads, models.DO_NOTHING, blank=True, null=True)
    push_id = models.CharField(max_length=255)
    enabled = models.IntegerField()
    mobile = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'push_ids'


class PushNotificationListXref(models.Model):
    notification = models.ForeignKey('PushNotifications', models.DO_NOTHING, primary_key=True)
    leadlist = models.ForeignKey(LeadLists, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'push_notification_list_xref'
        unique_together = (('notification', 'leadlist'),)


class PushNotificationStats(models.Model):
    notification = models.ForeignKey('PushNotifications', models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey(Leads, models.DO_NOTHING, blank=True, null=True)
    list = models.ForeignKey(LeadLists, models.DO_NOTHING, blank=True, null=True)
    ip = models.ForeignKey(IpAddresses, models.DO_NOTHING, blank=True, null=True)
    date_sent = models.DateTimeField()
    date_read = models.DateTimeField(blank=True, null=True)
    is_clicked = models.IntegerField()
    date_clicked = models.DateTimeField(blank=True, null=True)
    tracking_hash = models.CharField(max_length=255, blank=True, null=True)
    retry_count = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    tokens = models.TextField(blank=True, null=True)
    click_count = models.IntegerField(blank=True, null=True)
    last_clicked = models.DateTimeField(blank=True, null=True)
    click_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_notification_stats'


class PushNotifications(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=255)
    url = models.TextField(blank=True, null=True)
    heading = models.TextField()
    message = models.TextField()
    button = models.TextField(blank=True, null=True)
    utm_tags = models.TextField(blank=True, null=True)
    notification_type = models.TextField(blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    read_count = models.IntegerField()
    sent_count = models.IntegerField()
    mobile = models.IntegerField()
    mobilesettings = models.TextField(db_column='mobileSettings')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'push_notifications'


class Reports(models.Model):
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    system = models.IntegerField()
    source = models.CharField(max_length=255)
    columns = models.TextField(blank=True, null=True)
    filters = models.TextField(blank=True, null=True)
    table_order = models.TextField(blank=True, null=True)
    graphs = models.TextField(blank=True, null=True)
    group_by = models.TextField(blank=True, null=True)
    aggregators = models.TextField(blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    is_scheduled = models.IntegerField()
    schedule_unit = models.CharField(max_length=255, blank=True, null=True)
    to_address = models.CharField(max_length=255, blank=True, null=True)
    schedule_day = models.CharField(max_length=255, blank=True, null=True)
    schedule_month_frequency = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reports'


class ReportsSchedulers(models.Model):
    report = models.ForeignKey(Reports, models.DO_NOTHING)
    schedule_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reports_schedulers'


class Roles(models.Model):
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_admin = models.IntegerField()
    readable_permissions = models.TextField()

    class Meta:
        managed = False
        db_table = 'roles'


class SamlIdEntry(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    entity_id = models.CharField(max_length=255)
    expirytimestamp = models.IntegerField(db_column='expiryTimestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saml_id_entry'
        unique_together = (('id', 'entity_id'),)


class SmsMessageListXref(models.Model):
    sms = models.ForeignKey('SmsMessages', models.DO_NOTHING, primary_key=True)
    leadlist = models.ForeignKey(LeadLists, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sms_message_list_xref'
        unique_together = (('sms', 'leadlist'),)


class SmsMessageStats(models.Model):
    sms = models.ForeignKey('SmsMessages', models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey(Leads, models.DO_NOTHING, blank=True, null=True)
    list = models.ForeignKey(LeadLists, models.DO_NOTHING, blank=True, null=True)
    ip = models.ForeignKey(IpAddresses, models.DO_NOTHING, blank=True, null=True)
    date_sent = models.DateTimeField()
    tracking_hash = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    tokens = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_message_stats'


class SmsMessages(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=255)
    message = models.TextField()
    sms_type = models.TextField(blank=True, null=True)
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)
    sent_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sms_messages'


class StageLeadActionLog(models.Model):
    stage = models.ForeignKey('Stages', models.DO_NOTHING, primary_key=True)
    lead = models.ForeignKey(Leads, models.DO_NOTHING)
    ip = models.ForeignKey(IpAddresses, models.DO_NOTHING, blank=True, null=True)
    date_fired = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stage_lead_action_log'
        unique_together = (('stage', 'lead'),)


class Stages(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    weight = models.IntegerField()
    publish_up = models.DateTimeField(blank=True, null=True)
    publish_down = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stages'


class TweetStats(models.Model):
    tweet = models.ForeignKey('Tweets', models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey(Leads, models.DO_NOTHING, blank=True, null=True)
    twitter_tweet_id = models.CharField(max_length=255, blank=True, null=True)
    handle = models.CharField(max_length=255)
    date_sent = models.DateTimeField(blank=True, null=True)
    is_failed = models.IntegerField(blank=True, null=True)
    retry_count = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    favorite_count = models.IntegerField(blank=True, null=True)
    retweet_count = models.IntegerField(blank=True, null=True)
    response_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweet_stats'


class Tweets(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(Pages, models.DO_NOTHING, blank=True, null=True)
    asset = models.ForeignKey(Assets, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    media_id = models.CharField(max_length=255, blank=True, null=True)
    media_path = models.CharField(max_length=255, blank=True, null=True)
    text = models.CharField(max_length=280)
    sent_count = models.IntegerField(blank=True, null=True)
    favorite_count = models.IntegerField(blank=True, null=True)
    retweet_count = models.IntegerField(blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweets'


class UserTokens(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    authorizator = models.CharField(max_length=32)
    secret = models.CharField(unique=True, max_length=120)
    expiration = models.DateTimeField(blank=True, null=True)
    one_time_only = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_tokens'


class Users(models.Model):
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    locale = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    last_active = models.DateTimeField(blank=True, null=True)
    online_status = models.CharField(max_length=255, blank=True, null=True)
    preferences = models.TextField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VideoHits(models.Model):
    lead = models.ForeignKey(Leads, models.DO_NOTHING, blank=True, null=True)
    ip = models.ForeignKey(IpAddresses, models.DO_NOTHING)
    date_hit = models.DateTimeField()
    date_left = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    isp = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    code = models.IntegerField()
    referer = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    remote_host = models.CharField(max_length=255, blank=True, null=True)
    guid = models.CharField(max_length=255)
    page_language = models.CharField(max_length=255, blank=True, null=True)
    browser_languages = models.TextField(blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_id = models.IntegerField(blank=True, null=True)
    time_watched = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_hits'


class WebhookEvents(models.Model):
    webhook = models.ForeignKey('Webhooks', models.DO_NOTHING)
    event_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'webhook_events'


class WebhookLogs(models.Model):
    webhook = models.ForeignKey('Webhooks', models.DO_NOTHING)
    status_code = models.CharField(max_length=50)
    date_added = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webhook_logs'


class WebhookQueue(models.Model):
    webhook = models.ForeignKey('Webhooks', models.DO_NOTHING)
    event = models.ForeignKey(WebhookEvents, models.DO_NOTHING)
    date_added = models.DateTimeField(blank=True, null=True)
    payload = models.TextField()

    class Meta:
        managed = False
        db_table = 'webhook_queue'


class Webhooks(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    webhook_url = models.CharField(max_length=255)
    events_orderby_dir = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webhooks'


class Widgets(models.Model):
    is_published = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_by_user = models.CharField(max_length=255, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    checked_out_by = models.IntegerField(blank=True, null=True)
    checked_out_by_user = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    cache_timeout = models.IntegerField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'widgets'
