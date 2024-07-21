def area_circulo(a):
    return 3.14 * a ** 2
area_circulo(5)

def perimetro_circulo(a):
    return 2 * 3.14 * a
perimetro_circulo(4)

######## 0tro modo

# circulo.py

import math # para el valor de PI
def area_circulo(radio):
    return math.pi * radio ** 2

def perimetro_circulo(radio):
    return 2 * math.pi * radio
