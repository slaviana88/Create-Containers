from django.db import models
# Create your models here.


class Container(models.Model):
    name_owner = models.CharField(max_length=50, unique=True)
    name_container = models.CharField(max_length=50, blank=True, null=True)
    ssh_key = models.CharField(max_length=1000)
    status = models.CharField(max_length=8, default='waiting')
    container_ip = models.CharField(max_length=15, blank=True, null=True)
