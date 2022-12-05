from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-index'),
    path('about/', views.about, name='main-about'),
    path('login/', views.login, name='main-login'),
    path('lesson/', views.lesson, name='main-lesson'),
]