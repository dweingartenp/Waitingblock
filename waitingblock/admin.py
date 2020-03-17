from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Restaurant

admin.site.register(Restaurant)
