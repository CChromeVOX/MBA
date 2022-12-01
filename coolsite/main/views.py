from django.shortcuts import render, redirect
from .models import *



menu = [ "О сайте", "Войти"]


def index(request):
    types = StudentType.objects.all()
    return render(request, 'main/index.html', {'types': types,'menu': menu, 'title': 'Главная'})

def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О сайте'})

def lessons(request, lessid):
    print(request.GET)
   
def archive(request, year):
    print(request.GET)