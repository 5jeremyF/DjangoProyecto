from django.db import models

# Create your models here.

        
class Materia(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    creditos = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name="Materia"
        verbose_name_plural="Materia"
        ordering = ['descripcion']
    def __str__(self):
        return self.descripcion

class Profesores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False,null=True)
    cedula = models.CharField(max_length=10, blank=False,null=False)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    sueldo = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name="Profesores"
        verbose_name_plural="Profesores"
        ordering = ['nombre']
    def __str__(self):
        return self.nombre

    