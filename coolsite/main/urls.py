from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-index'),
    path('about/', views.about, name='main-about'),
    path('login/', views.custom_login, name='main-login'),
    path('lesson/', views.lesson, name='main-lesson'),
    path('logout/', views.logout_view, name='main-logout'),
]