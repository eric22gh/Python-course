from rest_framework import serializers  # type: ignore 
from amm.models import autorDB, Frasedb

#  serialoizador de modelo 
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = autorDB
        fields = '__all__' # o   # Esto incluye todos los campos del modelo

class FraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frasedb
        fields = '__all__' # o   # Esto incluye todos los campos del modelo
        
class AutorFraseSerializer(serializers.ModelSerializer):
    frases = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='frasedb-detail'  # Nombre de la vista para acceder a los detalles de la frase
    )
    # o frases = serializers.StringRelatedField(many=True) # para que devuelva el nombre de la frase en vez de la url
    class Meta:
        model = autorDB
        fields = "__all__"  

    class Meta:
        model = autorDB
        fields = '__all__'  # o   # Esto incluye todos los campos del modelo