from random import choice, randint, uniform
from django.core.management.base import BaseCommand
from homework.models import Product, Customer


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        customers = []
        for i in range(1, count + 1):
            customers.append(Customer(
                name=f'продукт номер {i}',
                email=f'mail{i}@gmail.com',
                phone=randint(82000000, 89999999),
                address=f'Adress{i}',
            ))
        Customer.objects.bulk_create(customers)

        products = []
        for i in range(1, count + 1):
            products.append(Product(
                title=f'продукт номер {i}',
                description='длинное описание продукта, которое и так никто не читает',
                price=uniform(0.50, 9999.99),
                amount=randint(1, 10_000),
            ))
        Product.objects.bulk_create(products)
