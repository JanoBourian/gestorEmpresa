from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

AS_BASE_TEMPLATE_DIR = 'entradas/'


class Inicio(TemplateView):
    template_name = AS_BASE_TEMPLATE_DIR + 'index.html'
