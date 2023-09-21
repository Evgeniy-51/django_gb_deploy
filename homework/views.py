from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
import logging
from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic import TemplateView

from homework.forms import ChangeProduct
from homework.models import Order, Customer, Product

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    html_content = """
    <h1> Это мой первый </h1>
    <h2> Django сайт </h2>
    """
    return HttpResponse(html_content)


def about_me(request):
    logger.info('About page accessed')
    html_content = """
    <h1> Это страничка </h1>
    <h2> про меня </h2>
    """
    return HttpResponse(html_content)


class ShowOrdersByClientId(TemplateView):
    template_name = "homework/show_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        if Customer.objects.filter(pk=client_id).exists():
            client = Customer.objects.get(pk=client_id)
            orders = Order.objects.filter(customer=client_id)
            context['name'] = client.name
            context['orders'] = orders
        return context


class ShowOrdersForAWeek(TemplateView):
    template_name = "homework/show_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        if Customer.objects.filter(pk=client_id).exists():
            client = Customer.objects.get(pk=client_id)
            res_date = datetime.now().date() - timedelta(days=7)
            orders = Order.objects.filter(customer=client_id).filter(create_date__date__gt=res_date)
            context['name'] = client.name
            context['orders'] = orders
        return context


class ShowOrdersForAMonth(ShowOrdersForAWeek):
    template_name = "homework/show_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        if Customer.objects.filter(pk=client_id).exists():
            client = Customer.objects.get(pk=client_id)
            res_date = datetime.now().date() - timedelta(days=30)
            orders = Order.objects.filter(customer=client_id).filter(create_date__date__gt=res_date)
            context['name'] = client.name
            context['orders'] = orders
        return context


class ShowOrdersForAYear(ShowOrdersForAWeek):
    template_name = "homework/show_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        if Customer.objects.filter(pk=client_id).exists():
            client = Customer.objects.get(pk=client_id)
            res_date = datetime.now().date() - timedelta(days=365)
            orders = Order.objects.filter(customer=client_id).filter(create_date__date__gt=res_date)
            context['name'] = client.name
            context['orders'] = orders
        return context


def change_product(request, prod_id):
    if request.method == 'POST':
        form = ChangeProduct(request.POST, request.FILES)

        if form.is_valid():
            req = request.POST
            prod = Product.objects.get(pk=req.get('prod_id'))

            image = form.cleaned_data['image']
            print(image)
            fs = FileSystemStorage()
            fs.save(image.name, image)

            prod.title = req.get('title')
            prod.description = req.get('description')
            prod.price = req.get('price')
            prod.amount = req.get('amount')
            prod.create_date = datetime.today()
            prod.image = form.cleaned_data['image']
            prod.save()

            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        prod = Product.objects.get(pk=prod_id)
        fill_form = {
            'prod_id': prod_id,
            'title': prod.title,
            'description': prod.description,
            'price': prod.price,
            'amount': prod.amount,
            'create_date': datetime.today(),
            'image': prod.image,
        }
        form = ChangeProduct(fill_form)

    return render(request, 'homework/change_prod.html', {'form': form})


def total_in_db(request):
    total = Product.objects.aggregate(Sum('amount'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'homework/total_amount.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.amount for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'homework/total_amount.html', context)


def total_in_property(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'homework/total_amount.html', context)