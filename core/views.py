from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')
def libro(request):
    return render(request,'core/libro.html')

def libros(request):
    return render(request,'core/libros.html')
def autores(request):
    return render(request,'core/autores.html')
def autor(request):
    return render(request,'core/autor.html')
