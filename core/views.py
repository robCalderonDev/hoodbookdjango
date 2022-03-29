from django.shortcuts import render
from .models import Libro ,Autor
from .forms import LibroForm

# Create your views here.
def home(request):
    libros = Libro.objects.all()
    autores= Autor.objects.all()
    data  ={  
        'libros':libros,
        'autores':autores
    }

    return render(request,'core/home.html',data)
def libro(request):
    return render(request,'core/libro.html')

def libros(request):
    return render(request,'core/libros.html')
def autores(request):
    return render(request,'core/autores.html')
def autor(request):
    return render(request,'core/autor.html')


def  agregar_libro(request):
    data = {
        'form': LibroForm()
    }

    if request.method=='POST':
        formulario = LibroForm(data = request.POST , files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] ="guardado correctamente"
        else:
            data["form"] = formulario
    return render(request,'core/libro/agregar.html',data)

def listar_libros(request):
    libros = Libro.objects.all()
    data = {
        'libros' :libros
    }

    return render(request,'core/libro/listar.html',data)