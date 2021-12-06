from django.urls import path
from articulos import views

urlpatterns=[
    path(
        route='',
        view=views.listar_articulos,
        name='index'
    ),
    path(
        route='create/',
        view=views.create_articulo,
        name='create'
    ),
    path(
        route='update/<int:id>/',
        view=views.update_articulo,
        name='update'
    ),
    path(
        route='delete/<int:id>/',
        view=views.delete_articulo,
        name='delete'
    ),
]