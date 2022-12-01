from django.db import models

# Create your models here.
class Discipline(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    def __str__(Discipline):
       return Discipline.title

class City(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    def __str__(City):
       return City.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    def __str__(Teacher):
       return Teacher.name


class Room(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(Room):
       return Room.title

class RequestStatus(models.Model):
    type = models.CharField(max_length=255)
    def __str__(RequestStatus):
       return RequestStatus.type

class StudentType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(StudentType):
       return StudentType.type

class Student(models.Model):
    type = models.ForeignKey(StudentType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    number = models.IntegerField()
    email = models.EmailField(max_length=255)
    def __str__(Student):
       return Student.name


class Group(models.Model):
    title = models.CharField(max_length=255)
    def __str__(Group):
       return Group.title


class GroupMember(models.Model):
    title = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(GroupMember):
       return str(GroupMember.student)

class Lesson(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(Lesson):
       return str(Lesson.discipline)

class Request(models.Model):
    student =  models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    def __str__(Request):
       return str(Request.student)

class LessonListeners(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(LessonListeners):
       return str(LessonListeners.student)




