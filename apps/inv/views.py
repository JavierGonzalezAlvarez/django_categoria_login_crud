from django.shortcuts import render

#Para que si un suario está logeado.
from django.contrib.auth.mixins import LoginRequiredMixin
#Importo las vistas genericas
from django.views import generic
#Bebe sacar los datos del modelo que necesitamos
from .models import Categoria

#El formulario lo importamos desde la vista
from .forms import class_Categoria_Form

#Importo reverse_lazy para decir a donde dirigir al hacer click
from django.urls import reverse_lazy

# Create your views here.
# La vista es lo que se ve en el formulario, una ver renderizado
#Creamos una clase con el mixin que tenemos y las vistas genericas de Django
class class_Categoria_View(LoginRequiredMixin, generic.ListView):
    #Esta vista debe tener unas catecteristicas a cumplir
    #Asignamos el modelo
    model = Categoria
    template_name = "inv/html_categoria_list.html"
    #Importante, el contexto es la variable que le va a pasar a la vista con
    # la informacion que va a renderizar a la plantilla. A la plantilla le dijimos
    # que se va a llamar obj, por defecto Dajgno le llama object, pero nosotros cambiamos 
    # el nombre con context_object_name
    context_object_name = "obj"
    #Si no estamos logeados, que nos pida logearnos
    #Si no estasmos redireccionados nos vamos a bases:html_login
    login_url = "bases:html_login"

#Creamos la vista del formulario.
#Con CreateView django ya va a interpretar que lo que se escribe es un insert en la BBDD
class class_Categoria_New_Form(LoginRequiredMixin, generic.CreateView):
    #Esta vista debe tener unas catecteristicas a cumplir
    #Asignamos el modelo
    model = Categoria
    template_name = "inv/html_categoria_form.html"
    #Importante, el contexto es la variable que le va a pasar a la vista con
    # la informacion que va a renderizar a la plantilla. A la plantilla le dijimos
    # que se va a llamar obj, por defecto Dajgno le llama object, pero nosotros cambiamos 
    # el nombre con context_object_name
    context_object_name = "obj"
    #Preguntamos que formulario va a renderizar
    form_class=class_Categoria_Form
    #Al dar submit que vaya a una URL. Al createView exige que se le diga
    #  a donde tiene que ir al hacer click
    success_url=reverse_lazy("inv:html_categoria_list")  #Es la ruta a donde va
    #Si no estamos logeados, que nos pida logearnos
    #Si no estasmos redireccionados nos vamos a bases:html_login
    login_url = "bases:html_login"
    
