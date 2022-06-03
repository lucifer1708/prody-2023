from django.contrib import admin
from .models import EventCard, Sponsors


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    search_fields = ['title', 'desc']


admin.site.register(EventCard, EventAdmin)
admin.site.register(Sponsors)
