from unicodedata import name
from django.urls import path
from django.urls import path
from .views import home,libros,autores,libro,autor,agregar_libro,listar_libros,modificar_libro,eliminar_libro

urlpatterns = [
    path('', home,name="home"),
    path('libros/',libros,name="libros"),
    path('autores/',autores,name="autores"),
    path('libro/<id>',libro,name="libro"),
    path('autor/<id>',autor,name="autor"),
    path('agregar-libro/',agregar_libro,name="agregar_libro"),
    path('listar-libros/',listar_libros,name="listar_libros"),
    path('modificar-libro/<id>/',modificar_libro,name="modificar_libro"),
    path('eliminar-libro/<id>/',eliminar_libro,name="eliminar_libro"),
    
   
]
