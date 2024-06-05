##### kwards todos los parametros en solo un parametro
def get_prod(**datos):
    print(datos["id"], datos["name"], datos["brand"])


get_prod(id="22", name="samsung", brand="TV")# bajo demanda
# {'id': 'id'} es un diccionario, es un tipo de datos