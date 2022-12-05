from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm


menu = [ "О Нас", "Войти"]


def index(request):
    types = StudentType.objects.all()
    return render(request, 'main/index.html', {'types': types,'menu': menu, 'title': 'Главная'})

def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О Нас'})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('main-about')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form, 'menu': menu, 'title': 'Вход на сайт'})

def lesson(request):
    error = 'No db'
    data = Lesson.objects.all()
    context = {
        'title':'Список текущих занятии',
        'header': 'Занятия',
        'data': data,
        'error': error,
    }
    return render(request, 'main/lesson.html', context)


def lessons(request, lessid):
    print(request.GET)
   
def archive(request, year):
    print(request.GET)

posts = [
    {
        'author': 'Админ',
        'title': 'Это первый пост',
        'content': 'Содержание первого поста.',
        'date_posted': 'декабрь 2022'
    },
    {
        'author': 'Пользователь',
        'title': 'Это второй пост',
        'content': 'Подробное содержание второго поста.',
        'date_posted': 'декабрь 2022'
    }
]


def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html', {'title': 'О Нас'})