from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('students/', views.alumnos, name="alumnes"),
    path('teachers/', views.profes, name="profes"),

    path('alumnes/info/<str:pk>/', views.infoAlumne, name="info_alum"), #informacion alumno individual
    path('profes/info/<str:pk>/', views.infoProfe, name="info_prof"),
    
    path('form/', views.formulario, name="form"),
    path('update/<str:pk>', views.actualizar_user, name="update"),
    path('delete/<str:pk>', views.delete_user, name='delete')
]