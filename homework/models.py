from django.db import models
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя")
    email = models.EmailField()
    phone = models.CharField(max_length=32, verbose_name="Телефон")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"
        ordering = ["reg_date", "name"]


class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Наличие")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    image = models.ImageField(blank=True, upload_to='images', verbose_name="Изображение")

    @property
    def total_amount(self):
        return sum(product.amount for product in Product.objects.all())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["title", "create_date"]


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Заказчик")
    products = models.ManyToManyField(Product, blank=True, related_name="products", verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Сумма")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Order {self.pk}, client  {self.customer}, sum {self.total_price}, products {self.products}"

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["create_date", "customer"]
