from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Discipline(models.Model):
    title = models.CharField('Наименование', max_length=255)
    about = models.TextField('Описание', blank=True)
    def __str__(self): 
       return f"{self.title}"
    
    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class City(models.Model):
    name = models.CharField('Наименование', max_length=255)
    about = models.TextField('Описание', blank=True)
    def __str__(self): 
       return f"{self.name}"
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Teacher(models.Model):
    name = models.CharField('ФИО преподавателя', max_length=255)
    about = models.TextField('Описание', blank=True)
    def __str__(self): 
       return f"{self.name}"
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Room(models.Model):
    title = models.CharField('Кабинет', max_length=255)
    address = models.CharField('Описание', max_length=255)
    def __str__(self): 
       return f"{self.title} - {self.address}"
    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

class RequestStatus(models.Model):
    type = models.CharField('Наименование статуса', max_length=255)
    def __str__(self):
       return f"{self.type}"
    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'

class StudentType(models.Model):
    type = models.CharField('Наименование вида', max_length=255)
    def __str__(self):
       return f"{self.type}"
    class Meta:
        verbose_name = 'Вид студента'
        verbose_name_plural = 'Виды студентов'

class Student(AbstractUser):
    type = models.ForeignKey(StudentType, on_delete=models.CASCADE, null=True)
    name = models.CharField('ФИО', max_length=255)
    number = models.IntegerField('Тел. номер',null=True)
    email = models.EmailField('Эл. почта', max_length=255)
    def __str__(self): 
       return f"{self.username} - {self.first_name} - {self.last_name} - {self.name}"
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Group(models.Model):
    title = models.CharField('Наименование группы',max_length=255)
    def __str__(self): 
       return f"{self.title}"
    class Meta:
        verbose_name = 'Группа студента'
        verbose_name_plural = 'Группы студентов'


class GroupMember(models.Model):
    title = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self): 
       return f"{self.title} - {self.student} "
    class Meta:
        verbose_name = 'Студент группы'
        verbose_name_plural = 'Студенты группы'

class Lesson(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField('Дата начала',)
    end_date = models.DateField('Дата окончания',)
    start_time = models.TimeField('Время начала',)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self): 
       return f"{self.discipline} - {self.city} - {self.start_date} "
    class Meta:
        verbose_name = 'Занятие (Расписание)'
        verbose_name_plural = 'Занятия (Расписание)'

class Request(models.Model):
    student =  models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField('Комментарии', blank=True)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    def __str__(self): 
       return f"{self.id} - {self.student.last_name}- {self.student.first_name} - {self.status} "
    class Meta:
        verbose_name = 'Запрос от студента'
        verbose_name_plural = 'Запросы от студентов'

class LessonListeners(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self): 
       return f"{self.lesson} - {self.student}"
    class Meta:
        verbose_name = 'Слушатель занятия'
        verbose_name_plural = 'Слушатели занятия'


