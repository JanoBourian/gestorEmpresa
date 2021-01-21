from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Departamento(models.Model):
    """
    Aquí se van a crear los campos del modelo Departamento
    Nombre:
    Nombre corto:
    Estado: 
    Fecha de creación:
    Usuario que creo el departamento: 
    """
    STATUS_CHOICES = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('pendiente', 'Pendiente')
    )

    nombre = models.CharField('Nombre', max_length=50, unique=True)
    nombre_corto = models.CharField('Alias', max_length=50, unique=True)
    estado = models.CharField('Estado', max_length=10, choices=STATUS_CHOICES)
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # Nombres
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        # Ordenamiento
        ordering = ['-fecha', 'nombre_corto', '-usuario']
        # No más de una combinación de registros
        unique_together = ('nombre', 'nombre_corto')

    def __str__(self):
        return f"{self.nombre}"
