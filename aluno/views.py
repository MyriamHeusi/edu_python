from django.shortcuts import render

def cadastrar(request):
    return render(request, 'aluno/cadastroAluno.html')

def listar(request):
    return render(request,'aluno/listarAluno.html')

