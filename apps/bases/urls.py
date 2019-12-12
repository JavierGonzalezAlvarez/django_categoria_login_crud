#Creo el fichero urls.py para crear las URLS donde apunta la LOGICA
from django.urls import path
#Importo las clases que tengo en "views"
#from .views import class_index
 
#Son las URL's de las paginas HTML que estan en la App
#Cuando tecleamos en el navegadior una url Django la busca es este diciconario/lista
urlpatterns = [
    #¿Que hay dentro?
    #path(route, view, kwargs=None, name=None)
    #path('una expresion en string', la clase o vista.as_view(), name='opcional url name'),
    #path('home' => en el navegador, me dará lo que ponga en 'home' => http://.../home)
    #path('' => indica que es la index porque llama a "class_index" primero)
    path('', class_index.as_view(), name='html_index'),   
    path('home', class_home.as_view(), name='html_home'),
]