from django.contrib import admin
from .models import Event, UserEventRegistration

# Register your models here.

admin.site.register(Event)
admin.site.register(UserEventRegistration)