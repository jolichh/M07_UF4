from django.db import models

# Create your models here.
# class Person(models.Model):
#     first_Name = models.CharField(max_length=100)

# class Alumno(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     email = models.EmailField()

# class Profe(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     email = models.EmailField()
#     curs = models.CharField(max_length=100)

class User(models.Model):
    ROLS = [
        ("a", "Alumne"),
        ("p", "Professor")
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    surname2 = models.CharField(max_length=100)
    email = models.EmailField()
    curs = models.CharField(max_length=100)
    rol = models.CharField(max_length=100, choices=ROLS)