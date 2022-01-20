from django.urls import path
from django.urls import path
from .views import home,libros,autores,libro,autor

urlpatterns = [
    path('', home,name="home"),
    path('libros/',libros,name="libros"),
    path('autores/',autores,name="autores"),
    path('libro/',libro,name="libro"),
    path('autor/',autor,name="autor"),
    
   
]
