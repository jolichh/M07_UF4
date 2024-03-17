from django.db import models

# Create your models here.
class Person(models.Model):
    first_Name = models.CharField(max_length=100)