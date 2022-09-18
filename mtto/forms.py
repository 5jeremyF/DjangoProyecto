from django import forms 
from .models import *


class MateriaForm(forms.ModelForm):
    class Meta: 
        model = Materia
        fields = ['descripcion','creditos','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese materia',
                'class':'form-group',
                'required': True,
            'creditos':forms.TextInput(attrs={
                'placeholder':'Ingrese creditos',
                'class': 'form-group',
                'required': True,

            })



            })
            
        }

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['nombre','cedula','materia','sueldo','estado']
        widgets = {
            'nombre':forms.TextInput(attrs={
                'placeholder':'Ingrese el nombre',
                'class':'form-group',
                'required': True
            }),
            
            'cedula':forms.TextInput(attrs={
                'placeholder':'Ingrese su número de cédula',
                'class':'form-group',
                'required': True
            }),

            

            'materia':forms.Select(attrs={
            'class':'form-group',
            'required': True
            }),

            'sueldo':forms.TextInput(attrs={
                'placeholder':'Ingrese el sueldo',
                'class':'form-group',
                'required':True
            })
        } 

def clean_estado(self):
    vali = self.cleaned_data.get('estado')

    if vali == True:
        return 'Activo'
    else: 
        return 'Inactivo'