from django.shortcuts import render, get_list_or_404 # es para redenrizar los templates, el get_list_or_404 es para lanzar un error si no cosigue lo que esta buscando
from .models import autorDB, Frasedb
from django.core.serializers import serialize # que hace serialize: convierte un objeto a json
from django.http import HttpResponse 

# Create your views here.
def IndexView(request):
    #pagina principal
   # return HttpResponse("hello word") # respuesta hppt
    objeto = autorDB.objects.all().order_by("id")
    return render(request, "Index.html", {"objeto": objeto}) # es la plantilla que esta en templates adentro de app 

def Autorview(request, id):
    autor =  get_list_or_404(autorDB, id=id)
    return render(request, "autor.html", {"objeto":autor})

##### vistas API #####
def AutorApi(request):
    autor = autorDB.objects.all() # un queryset que trae todos los objetos de la base de datos
    # autor = autorDB.objects.filter(id=1) # un queryset que trae todos los objetos de la base de datos del id 1
    data = serialize("json", autor) # serializa el objeto(los datos de la base de datos) a json
    return HttpResponse(data, content_type="application/json") # devuelve la respuesta en formato json