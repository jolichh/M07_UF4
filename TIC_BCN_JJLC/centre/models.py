from django.db import models

# Create your models here.
class Person(models.Model):
    first_Name = models.CharField(max_length=100)

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()

class Profe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    curs = models.CharField(max_length=100)