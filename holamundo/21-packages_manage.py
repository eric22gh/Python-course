###### Maneje de paquetes #####

# pip --version
# pip install pip
# pip install --upgrade pip
# pip install numpy
# pip list
# pip uninstall pandas
# pip install requests


import pandas as pd
import numpy as np
import requests as pt # peticiones a una api

print(np.version.version)

numpay_arry = np.array([22, 45, 56, 100, 45, 10,65])
print(type(numpay_arry))

print(numpay_arry * 3) # multiplica todos los numeros x 3

# peticiones a una api
respuesta = pt.get("https://pokeapi.co/api/v2/pokemon?limit=555")
print(respuesta)
print(respuesta.status_code)
print(respuesta.json())

# arithmetics package

import my_module as arithmetics

print(arithmetics.sumvalue(22, 87))



