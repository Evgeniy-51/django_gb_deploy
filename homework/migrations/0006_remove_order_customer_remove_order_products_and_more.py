# Generated by Django 4.2.5 on 2023-09-12 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0005_alter_order_customer_alter_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
