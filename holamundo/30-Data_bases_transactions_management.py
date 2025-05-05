# Dia 30: manejo de transacciones en bases de datos

# 🧠 Teoría
# una transacion es cuando se ejecuta una serie de operaciones en una base de datos y estas
# modifican el estado de la base de datos.

# commit: guarda los cambios realizados en la base de datos.
# rollback: deshace los cambios realizados en la base de datos.

import psycopg2 as pg2
# Conexión a la base de datos

conexion = pg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
# Crear un cursor
cursor = conexion.cursor()
# Crear una tabla
sql = '''
CREATE TABLE IF NOT EXISTS people(
    id_persons SERIAL PRIMARY KEY,
    name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50)
)'''
cursor.execute(sql)
conexion.commit() # guardar los cambios en la base de datos
# Insertar datos
sql = 'INSERT INTO people(name, last_name, email) VALUES(%s, %s, %s)'
var = ("maria", "hernandez", "mr@gmail.com")
cursor.execute(sql, var)
conexion.commit() # guardar los cambios en la base de datos


