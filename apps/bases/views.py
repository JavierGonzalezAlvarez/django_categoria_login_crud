from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views import generic

#from .forms import PaginaForm

#Django necesita que importemos estas clases en views.py
#Las mayusculas y minusculas importan en python
from django.http import HttpResponse  

#Añado Template
#from django.views.generic import TemplateView,

#Con esto me aparece context en el menu inteligente de VSC
from django.template import Template, Context

#import datetime
#Para devolver a una URL despues de una acción
from django.urls import reverse, reverse_lazy

#--------------------------------------------------------------
#Mixins
#Importo la Clase LoginRequiredMixin
#Para que si un suario está logeado, que pase a admin
from django.contrib.auth.mixins import LoginRequiredMixin
#--------------------------------------------------------------

# Create your views here.

#Clase que hereda de generic una clase llamada TemplateView
#Ahora le digo a Home que herede de Login... y de TemplateView
#Los mixin deben de colocarse a la izquierda. El orden es importante, para dar prioridad
#class Class_Home(generic.TemplateView):
class Class_Home(LoginRequiredMixin, generic.TemplateView):
    #class django.views.generic.base.TemplateView
    #This view inherits methods and attributes from the following views:
        #django.views.generic.base.TemplateResponseMixin
        #django.views.generic.base.ContextMixin
        #django.views.generic.base.View
    #Method Flowchart
        #setup()
        #dispatch()
        #http_method_not_allowed()
        #get_context_data()

    #TemplateView sólo tiene una propiedad.
    #Indico donde está la plantilla
    #Esta es la antigua =>  #template_name = "base/html_base.html"
    template_name = 'bases:html_home.html'
    #Indico el mixin para que si queireo ver la vista 'bases/html_home.html' 
    # y si no estoy autenticado me redirige al login.
    #Si intento entrar al home, me redirecciona a esta URL
    #login_url = '/admin'
    #Si intento entrar al home, me redirecciona a esta URL
    login_url = 'bases:html_login'
    