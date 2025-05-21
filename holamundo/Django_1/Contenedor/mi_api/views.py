from django.shortcuts import render # type: ignore
from rest_framework import  generics  # type: ignore
from amm.models import autorDB, Frasedb 
from .serializers import AutorSerializer, FraseSerializer, AutorFraseSerializer 
from  rest_framework import viewsets # type: ignore

# Create your views here.
class AutorList(generics.ListCreateAPIView):
    queryset = autorDB.objects.all()
    serializer_class = AutorSerializer 
    
class AutorListFrase(generics.ListCreateAPIView):
    queryset = autorDB.objects.all()
    serializer_class = AutorFraseSerializer
    
class AutorAPICreate(generics.CreateAPIView):
    queryset = autorDB.objects.all()
    serializer_class = AutorSerializer
    
class AutorApiRetrieve(generics.RetrieveAPIView):
    queryset = autorDB.objects.all()
    serializer_class = AutorSerializer
    
class AutorApiDestroy(generics.DestroyAPIView):
    queryset = autorDB.objects.all()
    serializer_class = AutorSerializer
    
#### lo anterior es muy repetitivo para esta viewset.
# viewsets.ModelViewSet es una clase que combina las funcionalidades de List, Create, Retrieve, Update y Destroy en una sola vista.
class frasedbViewSet(viewsets.ModelViewSet):
    queryset = autorDB.objects.all()
    serializer_class = FraseSerializer