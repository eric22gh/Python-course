# instalar postgresql y su coneccion con python, nota: pip install mysql-connector-python
# pip install psycopg2

import psycopg2 as pg2 # importamos la libreria psycopg2(se usa para conectarse a la base de datos)
# Conectarse a la base de datos
conexion = pg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db') # guardar la conexion en una variable
#print(conexion)

# Crear un cursor: es un objeto que permite ejecutar sentencias SQL en la base de datos
# cursor = conexion.cursor()

# sentencia SQL
# sql = 'SELECT * FROM persons WHERE id_persons = 3'
# cursor.execute(sql)
# personas = cursor.fetchall() # fetchall() devuelve una lista con los registros de la consulta
# print(personas)

# cursor.close()
# conexion.close()

# con bloques with y manejo de excepciones
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             #sql = 'SELECT * FROM persons WHERE id_persons = 3' # sentencia SQL entienden numeros en string
#             #sql = 'SELECT * FROM persons WHERE id_persons In (1, 2, 3)'
#             sql = 'SELECT * FROM persons'
#             cursor.execute(sql)
#             personas = cursor.fetchall()
#             #personas = cursor.fetchone() # fetchone() devuelve un solo registro
#             print(personas)

# except Exception as e:
#     print(f'Ocurrio un error: {e}')

# finally:
#     #cursor.close()
#     conexion.close()

# Insertar datos
try:
    with conexion:
        with conexion.cursor() as cursor:
            sql = 'INSERT INTO persons(name, last_name, email) VALUES(%s, %s, %s)'
            #cursor.execute(sql, ('Juan', 'Perez', 'JP@gmail.com'))
            # cursor.execute(sql, ('Maria', 'Lopez', 'Ml@gmail.com'))
            # cursor.execute(sql, ('Karla', 'Gomez', 'KG@gmail.com'))
            #conexion.commit() # confirmar la transaccion, cuando no se usa with

            # insertar varios registros
            registros = (
                ('carlos', 'villa', 'CV@gmail.com'),
                ('luis', 'castro', 'Lc@gmail.com')
            )  
            cursor.executemany(sql, registros) 
            print(f'se han insertado: {cursor.rowcount} registros correctamente')
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    #cursor.close() como se usa with no es necesario cerrar el cursor
    conexion.close()

# actualizar un dato
try:
    with conexion:
        with conexion.cursor() as cursor:
            sql = 'UPDATE persons SET name = %s, last_name = %s, email = %s WHERE id_persons = %s'
            cursor.execute(sql, ('Juan', 'Perez', 'PY@gmail.com')) # execute: ejecuta una sola consulta
            print(f'se han actualizado: {cursor.rowcount} registros correctamente')
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()

# actualizar varios datos 
try:
    with conexion:
        with conexion.cursor() as cursor:
            sql = 'UPDATE persons SET name = %s, last_name = %s, email = %s WHERE id_persons = %s'
            registros = (
                ('Maria', 'Lopez', 'Mo@gmail.com'),
                ('Karla', 'Gomez', 'Km@gmail.com')
            )
            cursor.executemany(sql, registros)
            print(f'se han actualizado: {cursor.rowcount} registros correctamente')
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()

# eliminar un registro
try:
    with conexion:
        with conexion.cursor() as cursor:
            sql = 'DELETE FROM persons WHERE id_persons = %s'
            cursor.execute(sql, (3,))
            print(f'se han eliminado: {cursor.rowcount} registros correctamente')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

# eliminar varios registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            sql = 'DELETE FROM persons WHERE id_persons = %s' # %s es un marcador de posicion
            registros = (4, 5)
            cursor.executemany(sql, registros)
            print(f'se han eliminado: {cursor.rowcount} registros correctamente')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()