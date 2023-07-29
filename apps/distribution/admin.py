from django.contrib import admin

from apps.distribution.models import Distribution, Message


# Register your models here.

class DistributionAdmin(admin.ModelAdmin):
    list_display = ['pk_id', 'start_time', 'end_time', 'text', 'filter']
    list_filter = ['pk_id']
    list_display_links = ['pk_id', 'start_time', 'end_time']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['pk_id', 'created_at', 'status', 'distribution', 'client']
    list_filter = ['pk_id', 'status']
    list_display_links = ['pk_id', 'created_at', 'status']


admin.site.register(Distribution, DistributionAdmin)
admin.site.register(Message, MessageAdmin)
