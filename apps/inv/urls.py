from django.urls import path
#De esta App importamos las vistas
from .views import class_Categoria_View, class_Categoria_New_Form
from .views import class_Categoria_Update_Form, class_Categoria_Delete_Form

urlpatterns = [
    path('categorias/', class_Categoria_View.as_view(), name='html_categoria_list'),
    path('categorias/new', class_Categoria_New_Form.as_view(), name='html_categoria_form'),
    path('categorias/update/<int:pk>', class_Categoria_Update_Form.as_view(), name='html_categoria_update'),
    path('categorias/delete/<int:pk>', class_Categoria_Delete_Form.as_view(), name='html_categoria_delete'),
]
