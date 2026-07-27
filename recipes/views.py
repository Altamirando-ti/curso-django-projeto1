# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Página raiz recipes')

def sobre(request):
    return HttpResponse('Página sobre')

def contato(request):
    return HttpResponse('Página contato')