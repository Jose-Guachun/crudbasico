from django.shortcuts import render, redirect
from articulos.forms import ArticuloForm
from articulos.models import Articulo

def listar_articulos(request):
    articulos=Articulo.objects.all().order_by('-created')
    return render(request, 'articulos/index.html',{'articulos':articulos})
    

def create_articulo(request):
    if request.method=='POST':
        form=ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articulos:index')
    else:
        form=ArticuloForm()
    return render(request, 'articulos/create_update.html', {'form':form, 'dato':True})

def update_articulo(request, id):
    articulo=Articulo.objects.get(id=id)
    if request.method=='GET':
        form=ArticuloForm(instance=articulo)
    else:
        form=ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulos:index')
    return render(request, 'articulos/create_update.html', {'form':form, 'dato':False})

def delete_articulo(request, id):
    articulo=Articulo.objects.get(id=id)
    descripcion=articulo.descripcion
    if request.method=='POST':
        articulo.delete()
        return redirect('articulos:index')
    return render(request, 'articulos/delete.html', {'descripcion':descripcion})
        
            
        

# Create your views here.
