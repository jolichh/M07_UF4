from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Context, loader 
from .form import FormularioUsers
from .models import User

# alum = [{"id":"1","name":"Joana","surname":"Lin", "email":"2023_joana.lin@iticbcn.cat"}, 
#             {"id":"2","name":"Oriana","surname":"Rojas", "email":"2023_oriana.rojas@iticbcn.cat"},
#             {"id":"3","name":"Veronica","surname":"Cartagena", "email":"2023_veronica.cartagena@iticbcn.cat"},
#             {"id":"4","name":"Gemma","surname":"Garrigosa", "email":"2023_gemma.garrigosa@iticbcn.cat"},
#             {"id":"5","name":"Adrià","surname":"Garcia", "email":"2023_adria.garcia@iticbcn.cat"},
#             {"id":"7","name":"Oscar","surname":"Perez", "email":"2023_oscar.perez@iticbcn.cat"},
#             {"id":"8","name":"Eric","surname":"Sanchez", "email":"2023_eric.sanchez@iticbcn.cat"},
#             {"id":"9","name":"Junhong","surname":"Zhu", "email":"2023_junhong.zhu@iticbcn.cat"},
#             {"id":"10","name":"Anxo","surname":"Aragundi", "email":"2023_anxo.aragundi@iticbcn.cat"},
#             {"id":"11","name":"Carlos andres","surname":"Zambrano", "email":"2023_carlos.zambrano@iticbcn.cat"},
#             {"id":"12","name":"Facundo Calixto","surname":"Barrios", "email":"2023_facundo.barrios@iticbcn.cat"},
#             {"id":"13","name":"Joel","surname":"Ghanem", "email":"2023_joel.ghanem@iticbcn.cat"},
#             {"id":"14","name":"Angelo","surname":"Montenegro", "email":"2023_angelo.montenegro@iticbcn.cat"},
#             {"id":"15","name":"Angel","surname":"Ivanov", "email":"2023_angel.ivanov@iticbcn.cat"},
#             {"id":"16","name":"Neus","surname":"Bravo", "email":"2023_neus.bravo@iticbcn.cat"},
#             {"id":"17","name":"Dinar","surname":"Khazimullin", "email":"2023_dinar.khazimullin@iticbcn.cat"},
#             ]

# prof = [{"id":"1", "name":"Roger","surname":"Sobrino", "email":"roger.sobrino@iticbcn.cat", "curs":"DAW i DAM"},
#               {"id":"2", "name":"Juanma","surname":"Sanchez", "email":"juanma.sanchez@iticbcn.cat", "curs":"DAW i DAM"},
#               {"id":"3", "name":"Xavi","surname":"Quesada", "email":"xavi.quesada@iticbcn.cat", "curs":"DAW i DAM"},
#               {"id":"4", "name":"Oriol","surname":"Roca", "email":"oriol.roca@iticbcn.cat", "curs":"DAW i DAM"},
#             ]

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

# muestra todos los alumnos (read)
def alumnos(request):    
    alumnos = User.objects.filter(rol='a')#accede a la base de datos de este modelo filtrando por rol
    context = {'alumnos': alumnos} 
    return render(request, 'alum.html', context)

# muestra todos los profesores (read)
def profes(request):
    profes = User.objects.filter(rol='p') #accede a la base de datos filtrando por rol
    context = {'profes': profes} 
    return render(request, 'prof.html', context)

# información sobre un alumno (read)
def infoAlumne(request, pk):
    alumno = User.objects.get(id=pk) # obtendrá aquel id que sea igual al pk 
    return render(request, 'info_alum.html', {'alumno':alumno})

# información sobre un profesor (read)
def infoProfe(request, pk):
    profe = User.objects.get(id=pk) # obtendrá aquel id que sea igual al pk 
    return render(request, 'info_prof.html', {'profe':profe})

# form alta usuari (create)
def formulario(request):    #create
    form = FormularioUsers()

    if request.method == 'POST':
        # pasar los datos del formulario
        form = FormularioUsers(request.POST)
        if form.is_valid():
            form.save()
            
            # redirigiar al template para mostrar los datos
            rol = form.cleaned_data.get('rol')
            if rol == 'p':
                return redirect('profes')
            elif rol == 'a':
                return redirect('alumnes')


    # volver a cargar formulario
    context = {'form':form}
    return render(request, 'form.html', context)

