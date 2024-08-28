from django.urls import path
from titulos import views

urlpatterns = [
    path('', views.cadastrar,name='cadastrar_titulos'),
    path('listar/', views.listar,name='listar_titulos'),
    path('cadastro/', views.cadastro,name='cadastro_titulos'),
]