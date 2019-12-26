#Traemos del Djago el modelo formulario por defecto que trae
from django import forms
from .models import Categoria
#Importo los modelos de formulario de Django
from django.forms import ModelForm

#Para grabar o actualizar un registro hay que crear un formulario
#  y así django podrá renderizar ese formulario
#El formularo es parecido a la vista, es decir se escribe lo que quiero renderizar
class class_Categoria_Form(forms.ModelForm):
    #Especificamos los datos con los que vamos a trabajar
    class Meta:
        #Con qué modelo trabajamos?
        model = Categoria
        #¿Qué campos usaremos o necesitamos?, serán los campos que el usuaio puede cambiar
        fields = ['descripcion','estado']
        #Especificamos las etiquetas. Para Descripcion que ponga => "Descripción de la categoria"
        labels = {'descripcion':"Descripción de la categoria",'estado':"Estado de la categoría"}
        #Usamos un widgte. Decimos ¿que tipo de objeto o input/elemento de HTML va a usar?
        #De forms. => usa un textinput
        widget = {'descripcion': forms.TextInput}

    #Como lo renderizo con Bootstrap, necesito que todos los elementos/input tengan la
    # clase de bootstrap form.control
    #Para esto sobreescribo el metodo init de este formulario, recibe els efl, argumentos y kwargs
    def __init__(self, *args, **kwargs):
        #Invovamos los elementos de la clase padre y le pasamos los argumentos, asi
        # nos aseguramos que el formulario se inicialice ya que estamos escribiendo
        # en su propio metodo
        super().__init__(*args, **kwargs)
        #¿Qué campos se van a mostrar?. Recorremos los campos a mostrar
        for campos_a_recorrer in iter(self.fields):
            #A ese campo que recorre, le asigna un Widget
            # y le asigna un atributo que va a cambiar
            self.fields[campos_a_recorrer].widget.attrs.update({
                #¿Qué va a cambiar?, la class, que le va a poner form.control
                'class': 'form.control'
            })

            #Form: Aqui decimos lo que va a mostrar
            #Plantilla: se encarga de renderizar lo que hemos puesto en form
            #Vista: toma el formulario y renderizarlo en la plantilla




