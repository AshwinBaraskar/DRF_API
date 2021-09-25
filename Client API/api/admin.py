from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'created_at', 'created_by']


admin.site.register(Client, ClientAdmin)
