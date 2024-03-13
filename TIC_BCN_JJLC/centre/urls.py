from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('alumnes/', views.alumnos, name="alumnes"),
    path('profes/', views.profes, name="profes"),
    path('alumnes/info_alumn/<int:pk>/', views.infoAlumne, name="info_alum") #informacion alumno individual
]