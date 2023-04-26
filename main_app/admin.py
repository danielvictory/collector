from django.contrib import admin

from .models import Event, Schedule

# Register your models here.
admin.site.register(Event)
admin.site.register(Schedule)