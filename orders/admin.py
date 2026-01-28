from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'address')
    list_filter = ('status',)
    search_fields = ('address',)
    ordering = ('-id',)


# Register your models here.
