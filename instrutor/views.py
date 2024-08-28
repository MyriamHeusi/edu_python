from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse('<h3>Esta é a página de Instrutor</h3>')

def fim(request):
    return HttpResponse('acabou!')

def cadastrar(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def listar(request):
    return render(request,'instrutor/listarInstrutor.html')
