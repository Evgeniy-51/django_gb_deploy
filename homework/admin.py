from django.contrib import admin

from homework.models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "address", "reg_date")
    list_display_links = ("name", "email", "phone", "address")
    search_fields = ("name", "phone")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "amount", "description")
    list_display_links = ("title",)
    search_fields = ("title", )

class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "quantity", "total_price", "create_date")
    list_display_links = ("customer", "create_date")
    search_fields = ("customer", )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
