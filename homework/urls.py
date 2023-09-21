from django.conf import settings
from django.conf.urls.static import static

from homework.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('about/', about_me, name='about'),
    path('orders/<int:client_id>/', ShowOrdersByClientId.as_view(), name='orders'),
    path('week/<int:client_id>/', ShowOrdersForAWeek.as_view(), name='week'),
    path('month/<int:client_id>/', ShowOrdersForAMonth.as_view(), name='month'),
    path('year/<int:client_id>/', ShowOrdersForAYear.as_view(), name='year'),
    path('change_prod/<int:prod_id>/', change_product, name='change_product'),
    path('total_db/', total_in_db, name='db'),
    path('total_view/', total_in_view, name='view'),
    path('total_property/', total_in_property, name='property'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)