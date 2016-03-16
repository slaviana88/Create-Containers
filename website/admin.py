from django.contrib import admin
from .models import Container
# Register your models here.


class ContainerAdmin(admin.ModelAdmin):
    list_display = ['name_container', 'name_owner', 'ssh_key', 'status', 'container_ip']

admin.site.register(Container, ContainerAdmin)
