from django.contrib import admin
from .models import GeneroPrimario, GeneroSecundario, Libro,Editorial,Autor,GeneroPrimario,GeneroSecundario,GeneroTerciario
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display  = ["nombre","sinopsis","paginas","idioma","editorial","fecha_estreno","autor","imagenLibro"]
    list_editable = ["sinopsis"]
    search_fields = ["nombre"]
    list_filter   = ["editorial","idioma"]
    list_per_page = 5


admin.site.register(Libro,LibroAdmin)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(GeneroPrimario)
admin.site.register(GeneroSecundario)
admin.site.register(GeneroTerciario)



