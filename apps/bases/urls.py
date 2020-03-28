#Creo el fichero urls.py para crear las URLS donde apunta la LOGICA
from django.urls import path
#Importo las clases que tengo en "views"
from .views import Class_Home
from django.contrib.auth import views as auth_views  

#Son las URL's de las paginas HTML que estan en la App
urlpatterns = [
    #¿Que hay dentro?
    path('', Class_Home.as_view(), name='html_home'),       
    path('login/',auth_views.LoginView.as_view(template_name='bases/html_login.html'), name='html_login'),
    #Ponemos la ruta de logout
    path('logout/',auth_views.LogoutView.as_view(template_name='bases/html_login.html'), name='logout'),
]