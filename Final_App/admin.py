from django.contrib import admin
from .models import Profile, doctors,appointment,contact

# Register your models here.

admin.site.register(Profile)
admin.site.register(doctors)
admin.site.register(appointment)
admin.site.register(contact)