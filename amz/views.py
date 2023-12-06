from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.

def hello(request):
    return HttpResponse("Hello, world = olá mundo ")

def amz(request):
    return render(request, 'usuario/home.html')

def cadastro(request):
    novo_item = Produto()
    novo_item.codigo_pro = request.POST.get('codigo_pro')
    novo_item.nome = request.POST.get('nome')
    novo_item.preco = request.POST.get('preco')
    novo_item.categoria = request.POST.get('categoria')
    novo_item.save()

    #mostra todos os itens 
    produtos = {
        'produtos' : Produto.objects.all()
    }

    #listagem de itens
    return render(request, 'usuario/itens.html', produtos)