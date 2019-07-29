from django.contrib import admin
from .models import users, doctors

# Register your models here.

admin.site.register(users)
admin.site.register(doctors)
