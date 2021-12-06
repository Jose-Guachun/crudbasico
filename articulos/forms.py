from django import forms
from django.forms import fields
from .models import *

class ArticuloForm(forms.ModelForm):
    class Meta:
        model=Articulo
        fields=('codigo', 'marca', 'descripcion', 'cantidad', 'precio')