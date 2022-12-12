
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime


menu = [ "О Нас", "Войти"]


def index(request):
    types = StudentType.objects.all()
    return render(request, 'main/index.html', {'types': types,'menu': menu, 'title': 'Главная'})

def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О Нас'})

def login_v(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password') 
            user = authenticate(request, username=username, password=password) 
            if user is not None: 
                login(request, user) 
                return redirect('main-about') 
            else: 
                print(request, "Why is this not returned for inval")       
    else: 
        form = AuthenticationForm() 
    return render(request, 'main/login.html', {'form': form, 'menu': menu, 'title': 'Вход на сайт'})

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


def mylesson(request):
    error = 'No db'
    current_user_lessons_id = LessonListeners.objects.filter(student = request.user).values_list('lesson_id')
    current_user_lessons = Lesson.objects.filter(id__in = current_user_lessons_id)
    context = {
        'title':'Список текущих занятии',
        'header': 'Занятия',
        'data': current_user_lessons,
        'error': error,
    }
    return render(request, 'main/mylessons.html', context)


def requests(request):
    error = 'No db'
    data = Request.objects.filter(student = request.user)
    context = {
        'title':'Список заявок',
        'header': 'Мои заявки',
        'data': data,
        'error': error,
    }
    return render(request, 'main/requests.html', context)


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
    return render(request, 'main/about.html', {'title': 'Высшая Школа Бизнеса AlmaU (ранее МАБ)'})


def coach(request):
    error = 'No db'
    data = Teacher.objects.all()
    context = {
        'title': 'Тренера',
        'header': 'Занятия',
        'data': data,
        'error': error,
    }
    return render(request, 'main/coach.html', context)


def disciplines(request):
    error = 'No db'
    data = Discipline.objects.all()
    context = {
        'title': 'Дисциплины',
        'header': 'Занятия',
        'data': data,
        'error': error,
    }
    return render(request, 'main/disciplines.html', context)

def select_view(request):
    form = RequestForm(request.POST)
    form.fields['lesson'].queryset = Lesson.objects.filter(start_date__gt = datetime.now())
    if request.POST:
        if form.is_valid():
            req = form.save(commit=False)
            req.student = request.user
            req.status = RequestStatus.objects.get(type="Отправлено")
            req.save()
        return redirect('main-about')


    return render(request, 'main/addrequest.html', {'form': form})