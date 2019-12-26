from django.urls import path

#De esta App importamos las vistas
from .views import class_Categoria_View, class_Categoria_New_Form

urlpatterns = [
    path('categorias/', class_Categoria_View.as_view(), name='html_categoria_list'),
    path('categorias/new', class_Categoria_New_Form.as_view(), name='html_categoria_form'),
]