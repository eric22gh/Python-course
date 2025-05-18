from django.urls import path
from .views import IndexView, Autorview, AutorApi

urlpatterns = [
    path(" ", IndexView),
    path("autor/<int:id>", Autorview, name="Autor"),
    path("api/list_autor", AutorApi, name="Autor_json")
]
