# import csv

# with open("file\\datos.csv") as archivo:
#     reader = csv.reader(archivo)
#     for row in reader:
#         print(row)

import pandas as pd
df = pd.read_csv("Datos.csv") # para que pandas lea todo el file
#df = pd.read_csv("Datos.csv",names=["Name","Age","City"])
print(df)
print(df["Edad"])

orden = df.sort_values("Ciudad")
print(orden)

orden_ascending = df.sort_values("Ciudad",ascending=False)
print(orden_ascending)

concatenando = pd.concat([df,df])
print(concatenando)

primera_fila = df.head(1) 

ultimas_filas = df.tail(2)

filas,comlumnas = df.shape # da el numero de fika y columnas del file csv