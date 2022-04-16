from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50);
    cita = models.TextField();
    historia = models.TextField();
    imagenAutor = models.ImageField(upload_to="libros", null=True)
    def __str__(self):
        return self.nombre


class Editorial (models.Model):
    nombre = models.CharField(max_length=50);

    def __str__(self):
        return self.nombre


class GeneroPrimario (models.Model):
   nombre=models.CharField(max_length=30);
    
   def __str__(self):
        return self.nombre

class GeneroSecundario (models.Model):
   nombre=models.CharField(max_length=30);
    
   def __str__(self):
        return self.nombre
class GeneroTerciario (models.Model):
   nombre=models.CharField(max_length=30);
    
   def __str__(self):
        return self.nombre



class Libro(models.Model):
    nombre = models.CharField(max_length=50);
    sinopsis = models.TextField();
    paginas = models.IntegerField();
    idioma = models.CharField(max_length=50);
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT);
    fecha_estreno = models.DateField();
    autor = models.ForeignKey(Autor,on_delete=models.PROTECT)
    imagenLibro = models.ImageField(upload_to="libros", null=True)
    generoPrimario = models.ForeignKey(GeneroPrimario, on_delete=models.PROTECT);
    generoSecundario = models.ForeignKey(GeneroSecundario, on_delete=models.PROTECT);
    generoTerciario = models.ForeignKey(GeneroTerciario, on_delete=models.PROTECT);

    def __str__(self):
       return  self.nombre

       
    
