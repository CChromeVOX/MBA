from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


menu = [ "О Нас", "Войти"]


def index(request):
    types = StudentType.objects.all()
    return render(request, 'main/index.html', {'types': types,'menu': menu, 'title': 'Главная'})

def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О Нас'})

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('main-about')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Здравствуйте, <b>{user.username}</b>! Вы успешно вошли в аккаунт")
                return redirect('main-about')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm() 
    
    return render(
        request=request,
        template_name="main/login.html", 
        context={'form': form}
        )

def logout_view(request):
    logout(request)
    return redirect('main-about')
    
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