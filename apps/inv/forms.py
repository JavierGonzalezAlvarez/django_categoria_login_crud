#Traemos del Djago el modelo formulario por defecto que trae
from djanfgo import from
from .models import Categoria

class class_Categoria_Form(forms.Modelform):
    #Especificamos los datos con los que vamos a trabajar
    class Meta:
        #Que modelo?
        Model=Categoria
        #Que campos usaremos o necesitamos?, serán los campos que el usuaio puede cambiar
        fields = ['descripcion','estado']
        #Especificamos las etiquetas. Para Descripcion que ponga => "Descripción de la categoria"
        labels = ['descripcion':"Descripción de la categoria",'estado':"Estado de la categoría"]
        #Usamos un widgte. Decimos ¿que tipo de objeto o input de HTML va a usar?
        #De forms. una un textinput
        widget={'descripcion': forms.textinput}

    #Como lo renderizo con bootstrap, necsito que todos los elementos/input tengan la
    #clase de bootstrap form.control
    #Para esto sobreescribo el metodo init de este formulario, recibe els efl, argumentos y kwargs
    def __init__(self, *args, **kwargs):
        #Invovamos el elemtnos de la clase padre y le pasamos los argumentos, asi
        #nos aseguramos que el formulario se inicialice ya que estamos escribiendo en su propio metodo
        super().__init__(*args, **kwargs)
        #¿Qué campos se va a mostrar?. Recorremos los campos a mostrar
        for campos_a_recorrer in iter(self.fields):
            #A ese campo que recorre le asigna un Widget
            #y le asigna un atributo que va a cambiar
            self.fields[campos_a_recorrer].widget.attrs.update({
                #¿Qué va a cambiar?, la class, que le va a poner form.control
                'class': 'form.control'
            })



