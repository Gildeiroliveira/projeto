from django.contrib import admin
from django.urls import path, include
from amz import views


urlpatterns = [
    #rota , views responsavel , nome de referencia
    path("admin/", admin.site.urls),
    path('hello', views.hello, name='hello'),
    path('', views.amz, name='home'),
    path('cadastro/', views.cadastro, name='Itens'),
    path('ver_d/', views.ver_d, name='ver'),
    path('delete/<int:codigo_pro>', views.delete, name='delete'),
    path('ver_itens', views.ver_itens, name='ver_itens'),
    path('editar', views.editar, name='editar'),
    path('update/<int:codigo_pro>', views.update, name='update')
]


