from django.contrib import admin
from .models import AddEvent, EventCard, Sponsors


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    search_fields = ['title', 'desc']

class AddEventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'name', 'email')
    search_fields = ['event_title', 'name', 'email']

admin.site.register(EventCard, EventAdmin)
admin.site.register(Sponsors)
admin.site.register(AddEvent, AddEventAdmin)
