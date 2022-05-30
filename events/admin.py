from django.contrib import admin
from .models import EventCard


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    search_fields = ['title', 'desc']


admin.site.register(EventCard, EventAdmin)
