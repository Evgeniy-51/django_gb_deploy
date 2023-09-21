from django.core.management.base import BaseCommand
from homework.models import Customer

class Command(BaseCommand):
    help = "Update client phone by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('phone', type=str, help='Client phone')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        phone = kwargs.get('phone')
        client = Customer.objects.filter(pk=pk).first()
        client.phone = phone
        client.save()
        self.stdout.write(f'{client}')