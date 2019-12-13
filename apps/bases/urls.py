#Creo el fichero urls.py para crear las URLS donde apunta la LOGICA
from django.urls import path
#Importo las clases que tengo en "views"
from .views import Class_Home
 
#Importamos las vistas de autenticacion para el Login
#Y le ponemos un alias auth_views
from django.contrib.auth import views as auth_views  

#Son las URL's de las paginas HTML que estan en la App
#Cuando tecleamos en el navegadior una url Django la busca es este diciconario/lista
urlpatterns = [
    #¿Que hay dentro?
    #path(route, view, kwargs=None, name=None)
    #path('una expresion en string', la clase o vista.as_view(), name='opcional url name'),
    #path('home' => en el navegador, me dará lo que ponga en 'home' => http://.../home)
    #path('' => indica que es la index porque llama a "class_index" primero)
    path('', Class_Home.as_view(), name='html_home'),   
    #path('home', class_home.as_view(), name='html_home'),

    #Ponemos una ruta nueva.
    #Cuando escribamos Login, utilizamos auth_view.LoginView .....
    #Reutilizamosuna vista luego pongo e indico donde esta la plantilla => as_view(template_name='bases/html_login.html')
    #A la URL le llamamos => name='html_login'
    path('login/',auth_views.LoginView.as_view(template_name='bases/html_login.html'), name='html_login'),

    #Ponemos la ruta de logout
    path('logout/',auth_views.LogoutView.as_view(template_name='bases/html_login.html'), name='logout'),
]