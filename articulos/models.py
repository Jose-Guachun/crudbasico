from django.db import models

class Marca(models.Model):
    descripcion=models.CharField(max_length=100)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.descripcion
        
class Articulo(models.Model):
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    codigo=models.CharField(max_length=10)
    descripcion=models.CharField(max_length=100)
    cantidad=models.IntegerField()
    precio=models.DecimalField(max_digits=8,decimal_places=2)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

