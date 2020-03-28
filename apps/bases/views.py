from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views import generic

from django.http import HttpResponse  


#Con esto me aparece context en el menu inteligente de VSC
from django.template import Template, Context

#Para devolver a una URL despues de una acción
from django.urls import reverse, reverse_lazy

#--------------------------------------------------------------
#Mixins
#Importo la Clase LoginRequiredMixin
#Para que si un suario está logeado, que pase a admin
from django.contrib.auth.mixins import LoginRequiredMixin
#--------------------------------------------------------------

# Create your views here.

class Class_Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/html_home.html'
    login_url = 'bases:html_login'
    