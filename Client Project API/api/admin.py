from django.contrib import admin
from .models import Client, Project


class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'created_at', 'created_by']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
