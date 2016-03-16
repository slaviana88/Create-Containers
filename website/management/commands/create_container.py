from django.core.management.base import BaseCommand
from website.apis import create_container_with_owner
from website.models import Container


class Command(BaseCommand):

    def handle(self, **options):
        waiting_containers = Container.objects.all().filter(status='waiting')

        for c in waiting_containers:
            owner = c.name_owner
            container = '{}/container'.format(owner)
            ssh = c.ssh_key
            c_IP = create_container_with_owner(container, owner, ssh)
            container_IP = c_IP.split("/")[0]
            c.name_owner = owner
            c.status = 'OK'
            c.container_ip = container_IP
            c.save()
