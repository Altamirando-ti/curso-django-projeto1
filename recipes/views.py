from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context= {'meuNome': 'Altamirando'})  #namespace

def sobre(request):
    return HttpResponse('Página sobre')

def contato(request):
    return render(request,'recipes/contato.html')