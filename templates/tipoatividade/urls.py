from django.urls import path
{% comment %} from tipoatividade.views import inicio
from tipoatividade.views import fim {% endcomment %}
from tipoatividade import views

urlpatterns = [
    #path('', inicio, name='inicio'),
    #path('fim/', fim, name='fim'),
    path('', views.cadastrar,name='cadastrar'),
    path('', views.listar,name='listar'),
]