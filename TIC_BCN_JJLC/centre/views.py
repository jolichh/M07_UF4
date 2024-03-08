from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader 

# Create your views here.
# def index(request):
#     professor = {"name":"Roger","surname":"Sobrino", "age":"17"}
#     template = loader.get_template('index_centre.html')
#     dades = template.render({'nombre': professor["name"], 'age': professor["age"]})
#     return HttpResponse(dades)

# def index(request):
#     professor = {"name":"Roger","surname":"Sobrino", "age":"18"}
    
#     return render(request, 'index_centre.html', {'nombre': professor["name"], 'age': professor["age"]})

def index(request):     
    template = loader.get_template('index.html')   
    return HttpResponse(template.render())

def alumnos(request):
    alum = [{"name":"Joana","surname":"Lin", "age":"18"}]
    context = {'alumnos': alum}
    return render(request, 'alum.html', context)

def profes(request):
    profes = [{"name":"Roger","surname":"Sobrino", "email":"rsobringo@itic.cat", "curs":"DAW i DAM"}]
    context = {'profe':profes}
    return render(request, 'prof.html', context)