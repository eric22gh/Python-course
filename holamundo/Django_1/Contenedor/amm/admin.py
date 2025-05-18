from django.contrib import admin
from .models import autorDB, Frasedb
# Register your models here.
admin.site.site_header = "welcome to the administrador page" # para cambiar o editar la cabecera de la pagina)admi
admin.site.index_title = "I am Eric Hernandez Edawrds" # para un subtitulo
admin.site.site_title = "hello" # para la pestaña de arriba en la pagina
class fraseInline(admin.TabularInline):
    model = Frasedb
    extra = 1

class Admin_su(admin.ModelAdmin):
    fields = ["name", "born_date", "die_date", "Profession", "country"]
    list_display = ["name", "born_date"]

    inlines = [fraseInline]

    def update(self, request, query):
        for obj in query:
            if "O" in obj.name:
                name1 = obj.name
                obj.name = name1.replace("O", "o")
                obj.save()
        self.message_user(request, "succesfuly")
    update.short_description = "update letter o"

    actions = ["update letter o"]

admin.site.register(autorDB, Admin_su)
@admin.register(Frasedb)
class frase_admin(admin.ModelAdmin):
    fields = ["appointment", "autor_fk"]
    list_display = ["appointment"]

# forma mas facil de registrar: con un decorador



    
