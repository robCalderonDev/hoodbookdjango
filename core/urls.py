from unicodedata import name
from django.urls import path
from django.urls import path
from .views import home,libros,autores,libro,autor,agregar_libro,listar_libros

urlpatterns = [
    path('', home,name="home"),
    path('libros/',libros,name="libros"),
    path('autores/',autores,name="autores"),
    path('libro/',libro,name="libro"),
    path('autor/',autor,name="autor"),
    path('agregar-libro/',agregar_libro,name="agregar_libro"),
    path('listar-libros/',listar_libros,name="listar_libros")
    
   
]
