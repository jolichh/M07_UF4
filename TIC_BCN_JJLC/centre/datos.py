# from centre.models import Alumno
# from centre.models import Profe

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

# # Añade los alumnos
# for datos_alumno in alum:
#     Alumno.objects.create(
#         id=datos_alumno['id'],
#         nombre=datos_alumno['name'],
#         apellido=datos_alumno['surname'],
#         email=datos_alumno['email']
#     )

# # Añade los profesores
# for datos_profesor in prof:
#     Profe.objects.create(
#         id=datos_profesor['id'],
#         nombre=datos_profesor['name'],
#         apellido=datos_profesor['surname'],
#         email=datos_profesor['email'],
#         curso=datos_profesor['curs']
#     )