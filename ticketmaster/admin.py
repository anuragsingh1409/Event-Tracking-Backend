from django.contrib import admin
from .models import Event
# Register your models here.

# class EventAdmin(admin):
#     list_display= ("id", "category","keyword","distance","Location")

admin.site.register(Event)
