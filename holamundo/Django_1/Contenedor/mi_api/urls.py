from django.urls import path
from .views import AutorList, AutorAPICreate, AutorApiRetrieve, AutorApiDestroy, frasedbViewSet, AutorListFrase
from rest_framework.routers import DefaultRouter # un router es una clase que se encarga de crear las URL para las vistas de un ViewSet.
# es un canalizardor que recive las peticiones y las redirige a la vista correspondiente.

router = DefaultRouter()  # Crear una instancia del router
router.register(r'frasedb', frasedbViewSet, basename='frasedb')  # Registrar el ViewSet con el router

urlpatterns = [
    path('autores/', AutorList.as_view(), name='autor-list'),  # URL para la lista de autores
    path('autores/create/', AutorAPICreate.as_view(), name='autor-create'),  # URL para crear un nuevo autor
    path('autores-retrieve/<int:pk>/', AutorApiRetrieve.as_view(), name='autor-read'),  # URL para obtener un autor específico por ID
    path('autores-destroy/<int:pk>/', AutorApiDestroy.as_view(), name='autor-destroy'),  # URL para obtener un autor específico por ID
    path('autores-frase/', AutorListFrase.as_view(), name='autor-frase'),  # URL para la lista de autores con frases
]

urlpatterns += router.urls  # Agregar las URLs generadas por el router a urlpatterns