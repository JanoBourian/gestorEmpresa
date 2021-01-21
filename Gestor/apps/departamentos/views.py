from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Departamento
# Create your views here.


class ListaDepartamentos(ListView):
    template_name = 'departamentos/lista.html'
    context_object_name = 'departamentos'
    Model = Departamento

    def get_queryset(self):
        todos = Departamento.objects.all()
        return todos
