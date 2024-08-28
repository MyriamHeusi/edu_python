from django.urls import path
from tipoatividade import views

urlpatterns = [
    path('', views.cadastrar,name='cadastrar_tipoatividade'),
    path('listar/', views.listar,name='listar_tipoatividade'),
]