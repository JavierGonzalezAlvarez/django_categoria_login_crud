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
from django.urls import reverse

# Create your views here.

#Clase que hereda de generic una clase llamada TemplateView
class Home(generic.TemplateView):
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

    #TemplateView sólo tiene una propiedad
    template_name = "base/base.html"
