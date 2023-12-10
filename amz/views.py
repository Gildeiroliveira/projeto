from django.shortcuts import render, redirect
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

def delete(request, codigo_pro):
    produto = Produto.objects.get(codigo_pro = codigo_pro)
    produto.delete()
    return redirect(ver_d)

def ver_d(request):
    produtos = {
        'produtos' : Produto.objects.all()
    }
    return render(request, 'usuario/delete.html', produtos)

def ver_itens (request):
    produtos =  Produto.objects.all()
    return render(request, 'usuario/itens.html', {'produtos' : produtos})

def editar(request):
    produtos = {
        'produtos' : Produto.objects.all()
    }
    return render(request, 'usuario/editar.html', produtos)

def update(request, codigo_pro):
    produtos = Produto.objects.get(codigo_pro = codigo_pro)
    return render(request, 'usuario/update.html', {'produtos':produtos})