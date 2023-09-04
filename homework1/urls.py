from homework1.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('about/', about_me, name='about'),
]
