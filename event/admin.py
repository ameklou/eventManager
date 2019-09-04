from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class EventAdmin(SummernoteModelAdmin):
    summernote_fields='description'
    list_display=['title','owner','price','date','location']
    list_filter=['title','owner','location','date']

admin.site.register(Event,EventAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display=['event','customer','number']
admin.site.register(Ticket,TicketAdmin)
