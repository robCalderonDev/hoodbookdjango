from django import forms
from .widgets import DatePickerInput
from .models import Libro

class ExampleForm(forms.Form):
        my_date_field = forms.DateField(widget=DatePickerInput)
       

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields= '__all__'
        widgets ={
            
            'fecha_estreno' : DatePickerInput(),
            
        }