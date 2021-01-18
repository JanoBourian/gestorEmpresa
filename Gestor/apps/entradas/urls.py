from django.contrib import admin
from django.urls import path
from .views import Inicio

app_name = 'entradas'


urlpatterns = [
    path('', Inicio.as_view(), name='inicio')
]
