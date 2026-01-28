from django.contrib import admin
from .models import Items

@admin.register(Items)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "price", "image")