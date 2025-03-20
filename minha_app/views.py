from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')  

def cadastro(request):
    return render(request, 'cadastro.html')

def listagem(request):
    return render(request, 'listagem.html')  

def receitas(request):
    return render(request, 'receitas.html')