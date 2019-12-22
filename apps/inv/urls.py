from django.urls import path

#De esta App importamos las vistas
from .views import class_CategoriaView

urlpatterns = [
    path('categorias/', class_CategoriaView.as_view(), name='html_categoria_list'),
]