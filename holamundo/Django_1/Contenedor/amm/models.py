from django.db import models
# Create your models or data base here.

class autorDB(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    born_date = models.DateField(verbose_name="born date", null = False, blank = False) # datefiel solo guarda la fecha
    die_date = models.DateField(verbose_name = "Die date", null = True, blank =True ) # daTETIMEFIELD GUARDA LA FECHA Y HORA, null es permitir campos nulos
    Profession = models.CharField(verbose_name = "Profession", max_length=50)
    country = models.CharField(verbose_name = "country", max_length=50)

    class Meta:
        db_table = "actors"
        verbose_name = "autor"
        verbose_name_plural = "actors"

    def __str__(self) -> str:
        return self.name # si se manda alguna peticion o registro va a devolver el nombre de el autor
            
    
class Frasedb(models.Model):
    appointment = models.TextField(verbose_name = "appointment", max_length=400)
    autor_fk = models.ForeignKey(autorDB, on_delete=models.CASCADE, related_name="frases") # on_delete=models.CASCADE elimina todas las frases del autor si se elimina el autor

class Meta:
        verbose_name = "autor"
        verbose_name_plural = "actors"
        
def __str__(self):
        return self.appointment # si se manda alguna peticion o registro va a devolver el nombre de el autor
