from django.shortcuts import render,redirect,get_object_or_404
from .models import GeneroPrimario, Libro ,Autor
from .forms import LibroForm
from django.contrib  import messages
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.
def home(request):
    libros = Libro.objects.all()
    autores= Autor.objects.all()
    
    librosReverse= libros[::-1]
    primerosLibros= librosReverse[0:4]
    data  ={  
        'libros':primerosLibros,
        'autores':autores
    }

    return render(request,'core/home.html',data)
    
def libro(request,id):
    libro = get_object_or_404(Libro,id=id)
    
    data={
        'libro':libro
    }
    
    return render(request,'core/libro.html',data)

def libros(request):
    libros = Libro.objects.all()
    generoPrimario = GeneroPrimario.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(libros,6)
        libros = paginator.page(page)
    except:
        raise Http404
    data ={
        'libros':libros,
        'paginator':paginator,
        'generoPrimario':generoPrimario,
       
    }
    return render(request,'core/libros.html',data)

def autores(request):
    autores = Autor.objects.all()
    data ={
        'autores':autores
    }

   
    return render(request,'core/autores.html',data)



def autor(request,id):
    autor = get_object_or_404(Autor,id=id)
    data={
        'autor':autor
    }
    return render(request,'core/autor.html',data)


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
    page = request.GET.get('page', 1)

    try:
        paginator =Paginator(libros, 5)
        libros = paginator.page(page)
    except:
        raise Http404



    data = {
        'entity' :libros,
        'paginator':paginator,
    }

    return render(request,'core/libro/listar.html',data)

def modificar_libro(request,id):
    libro =get_object_or_404(Libro,id=id)
    data={
        'form':LibroForm(instance=libro)
    }
    if request.method =='POST':
        formulario =LibroForm(data =request.POST, instance=libro,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="listar_libros")
        data["form"] = formulario
        
    
    return render(request,'core/libro/modificar.html',data)

def eliminar_libro(request,id):
    libro = get_object_or_404(Libro,id=id)
    libro.delete()
    messages.success(request,"Eliminado correctamente")

    return redirect(to ="listar_libros")

