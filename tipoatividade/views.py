from django.shortcuts import render
from tipoatividade.models import TipoAtividade

# Create your views here.
def cadastrar(request):
    return render(request, 'tipoatividade/cadastroTiposAtividade.html')

def listar(request):
    
    registros = TipoAtividade.objects.all()
    
    contexto ={'tipo_atividade_lista': registros}

    return render(request,'tipoatividade/listarTiposAtividade.html', contexto)
