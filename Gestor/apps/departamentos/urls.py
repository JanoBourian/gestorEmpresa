from django.contrib import admin
from django.urls import path
from .views import ListaDepartamentos

app_name = 'departamentos'


urlpatterns = [
    path('lista/', ListaDepartamentos.as_view(), name='lista'),
]
