from django.shortcuts import render
#Para que si un suario está logeado.
from django.contrib.auth.mixins import LoginRequiredMixin
#Importo las vistas genericas
from django.views import generic
#Bebe sacar los datos del modelo que necesitamos
from .models import Categoria
#El formulario creado lo importamos desde la vista
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
    # que se va a llamar obj, por defecto Djagno le llama object, pero nosotros cambiamos 
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
    form_class = class_Categoria_Form
    #Al dar submit que vaya a una URL. Al createView exige que se le diga
    #  a donde tiene que ir al hacer click
    #Es la ruta a donde va una vez que se crea el registro. El createView exige que se redireccione
    success_url = reverse_lazy("inv:html_categoria_list")  
    #Si no estamos logeados, que nos pida logearnos y nos vamos a bases:html_login
    login_url = "bases:html_login"
    
    #Cuando creamos el modelo habia una propiedad "crear usuario" con una foreingkey (id), 
    # no podiamos crear dos id.
    #Vamos a sobreescribir la propiedad, el metodo form_valid de esta vista para poder tener
    #  acceso a la informacion que se esta procesando o lo que se envia desde le formulario
    #  de ahí podemos coger datos de usuario que lo está procesando y manejar los datos del usuario
    def form_valid(self, form):
        #Accedemos al formulario desde este metodo
        #uc = usuario crear
        #con self.request.user cogemos el id del usuario (logeado) que está creando el formulario
        #Lo guarda en el formulario. Cogemos el usuario que crea el registro que era el campo "uc"
        form.instance.uc = self.request.user
        #Debemos retornar si el formulario es valido. Lo ahremos sobre el Padre con super()
        #Le mandamos el formulario que hemos modificado
        return super().form_valid(form)

#La Vista, va a ser igual que la createview, pero UpdateView
#Con poner CreateView, Django va a actualizar el registro
class class_Categoria_Update_Form(LoginRequiredMixin, generic.UpdateView):
    #Esta vista debe tener unas caracteristicas a cumplir
    #Asignamos el modelo
    model = Categoria
    template_name = "inv/html_categoria_form.html"
    #Importante, el contexto es la variable que le va a pasar a la vista con
    # la informacion que va a renderizar a la plantilla. A la plantilla le dijimos
    # que se va a llamar obj, por defecto Dajgno le llama object, pero nosotros cambiamos 
    # el nombre con context_object_name
    context_object_name = "obj"
    #Preguntamos que formulario va a renderizar
    form_class = class_Categoria_Form
    #Al dar submit que vaya a una URL. Al createView exige que se le diga
    #  a donde tiene que ir al hacer click
    #Es la ruta a donde va una vez que se crea el registro. El createView exige que se redireccione
    success_url = reverse_lazy("inv:html_categoria_list")  
    #Si no estamos logeados, que nos pida logearnos y nos vamos a bases:html_login
    login_url = "bases:html_login"
    
    #Cuando creamos el modelo habia una propiedad "crear usuario" con una foreingkey (id), no podiamos crear dos id
    #Vamos a sbreescribir la propiedad, el metodo form_valid de etsa vista para poder tener
    #  acceso a la informacion que se esta procesando o lo que se envia desde le formulario
    #  de ahí podemos coger datos de usuario que lo está procesando y manajar los datos del usuario
    def form_valid(self, form):
        #Accedemos al formulario desde este metodo                
        #Lo guarda en el formulario. Cogemos el campo "um", que es el usuario que modifica el registro
        #Coloco el user.id porque no lo puedo referencia con el foreignkey (este era para el uc), 
        #  En este caso um es un intgeger => um = models.IntegerField(null=True, blank=True)
        form.instance.um = self.request.user.id
        #Debemos retornar si el formulario es valido. Lo ahremos sobre el Padre con super()
        #Le mandamos el formulario que hemos modificado
        return super().form_valid(form)


class class_Categoria_Delete_Form(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "inv/html_categoria_delete_form.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:html_categoria_list")  
    login_url = "bases:html_login"
    