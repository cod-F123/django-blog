from django.contrib import admin
from .models import Profile , Following
from django.contrib.auth.models import User 

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]

admin.site.register(Following)
    
