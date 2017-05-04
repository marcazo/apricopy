from django.contrib import admin
from .models import Event

class EventModelAdmin(admin.ModelAdmin):
    list_display = ["title", "time", "address"]
    search_fields = ["title", "description"]

admin.site.register(Event, EventModelAdmin)