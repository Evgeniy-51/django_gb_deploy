from django.core.management.base import BaseCommand
from homework.models import Customer


class Command(BaseCommand):
    help = "Create customer."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='email')
        parser.add_argument('phone', type=str, help='phone')
        parser.add_argument('address', type=str, help='address')
    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        client = Customer(name=name, email=email, phone=phone, address=address)
        client.save()
        self.stdout.write(f'{client}')

    # python manage.py add_client John johnsilver@gmail.com 899956787545 "5-st avenue, 67"





