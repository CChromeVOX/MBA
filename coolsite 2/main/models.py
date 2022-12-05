from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Discipline(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    def __str__(self): 
       return f"{self.title} "


class City(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    def __str__(self): 
       return f"{self.name} | {self.about}"

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    def __str__(self): 
       return f"{self.name} "


class Room(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self): 
       return f"{self.title} | {self.address}"

class RequestStatus(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
       return f"{self.type}"

class StudentType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
       return f"{self.type}"

class Student(AbstractUser):
    type = models.ForeignKey(StudentType, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    number = models.IntegerField(null=True)
    email = models.EmailField(max_length=255)
    def __str__(self): 
       return f"{self.name} | {self.type} "


class Group(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): 
       return f"{self.title}"


class GroupMember(models.Model):
    title = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self): 
       return f"{self.title} | {self.student}  "

class Lesson(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self): 
       return f"{self.discipline} | {self.city} | {self.start_date} "

class Request(models.Model):
    student =  models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    def __str__(self): 
       return f"{self.student} | {self.status} "

class LessonListeners(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self): 
       return f"{self.lesson} | {self.student}"




