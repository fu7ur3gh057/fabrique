from django.contrib import admin

from apps.client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ['pk_id', 'operator_code', 'phone_number', 'tag', 'timezone']
    list_filter = ['pk_id']
    list_display_links = ['pk_id', 'operator_code', 'tag']


admin.site.register(Client, ClientAdmin)
