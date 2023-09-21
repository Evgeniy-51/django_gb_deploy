from django.core.management.base import BaseCommand
from homework.models import Product


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='title')
        parser.add_argument('description', type=str, help='description')
        parser.add_argument('price', type=int, help='price')
        parser.add_argument('amount', type=int, help='amount')
    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        price = kwargs.get('price')
        amount = kwargs.get('amount')

        prod = Product(title=title, description=description, price=price, amount=amount)
        prod.save()
        self.stdout.write(f'{prod}')

    # python manage.py





