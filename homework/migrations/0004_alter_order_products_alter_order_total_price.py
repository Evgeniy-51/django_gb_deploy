# Generated by Django 4.2.5 on 2023-09-12 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_remove_order_products_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='homework.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
