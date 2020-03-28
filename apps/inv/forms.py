from django import forms
from .models import Categoria
from django.forms import ModelForm

class class_Categoria_Form(forms.ModelForm):
    #Especificamos los datos generales con los que vamos a trabajar
    class Meta:
        #Con qué modelo trabajamos?
        model = Categoria
        #¿Qué campos usaremos o necesitamos?, serán los campos que el usuaio puede cambiar
        fields = ['descripcion','estado']
        #Especificamos las etiquetas. Para Descripcion que ponga => "Descripción de la categoria"
        labels = {'descripcion':"Descripción de la categoria",'estado':"Estado de la categoría"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #¿Qué campos se van a mostrar?. Recorremos los campos a mostrar
        for campos_a_recorrer in iter(self.fields):
            self.fields[campos_a_recorrer].widget.attrs.update({
                'class': 'form-control'
            })
           




