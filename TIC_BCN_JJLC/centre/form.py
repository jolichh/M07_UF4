from django.forms import ModelForm
from .models import User

class FormularioUsers(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # opcion para seleccionar atributos especificos de la classe
        # field = ['id', 'first_Name', 'lastName', 'age']