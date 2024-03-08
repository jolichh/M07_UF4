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
    template = loader.get_template('index_centre.html')   
    return HttpResponse(template.render())

def alumnos(request):
    alum = [{"id":"1","name":"Joana","surname":"Lin", "email":"2023_joana.lin@iticbcn.cat"}, 
            {"id":"2","name":"Oriana","surname":"Rojas", "email":"2023_oriana.rojas@iticbcn.cat"},
            {"id":"3","name":"Veronica","surname":"Cartagena", "email":"2023_veronica.cartagena@iticbcn.cat"},
            {"id":"4","name":"Gemma","surname":"Garrigosa", "email":"@iticbcn.cat"},
            {"id":"5","name":"Joana","surname":"Lin", "email":"@iticbcn.cat"},
            {"id":"6","name":"Joana","surname":"Lin", "email":"@iticbcn.cat"}]
    context = {'alumnos': alum}
    return render(request, 'alum.html', context)

def profes(request):
    profes = [{"id":"1", "name":"Roger","surname":"Sobrino", "email":"roger.sobrino@iticbcn.cat", "curs":"DAW i DAM"},
              {"id":"2", "name":"Juanma","surname":"Sanchez", "email":"roger.sobrino@iticbcn.cat", "curs":"DAW i DAM"},
              {"id":"3", "name":"Xavi","surname":"Sobrino", "email":"roger.sobrino@iticbcn.cat", "curs":"DAW i DAM"},
              {"id":"4", "name":"Oriol","surname":"Sobrino", "email":"roger.sobrino@iticbcn.cat", "curs":"DAW i DAM"},
              ]
    context = {'profes':profes}
    return render(request, 'prof.html', context)