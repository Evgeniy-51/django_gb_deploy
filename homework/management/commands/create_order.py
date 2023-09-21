from django.core.management.base import BaseCommand
from homework.models import Customer, Product, Order


class Command(BaseCommand):
    help = "Add items to order."

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID')
        parser.add_argument('product_id', type=int, help='Product ID')
        parser.add_argument('quantity', type=int, help='quantity')

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('client_id')
        product_id = kwargs.get('product_id')
        quantity = kwargs.get('quantity')
        client = Customer.objects.get(pk=client_id)
        item = Product.objects.get(pk=product_id)
        amount = item.amount
        total_price = item.price * quantity

        if  amount - quantity >= 0:
            order = Order.objects.create()
            order.customer = client
            order.products.add(item)
            order.quantity = quantity
            order.total_price = total_price
            item.amount = amount - quantity
            order.save()
            item.save()



