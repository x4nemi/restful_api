import mysql.connector

bd = mysql.connector.connect(
    user = 'ximena', password = '123',
    database = 'cinemapp'
)

cursor = bd.cursor() #lo que hará la conexión del
                     #script y la base de datos

def get_usuarios():
    consulta = "SELECT * FROM usuario"

    cursor.execute(consulta)
    usuarios = []
    for row in cursor.fetchall():
        usuario = {
            "id": row[0],
            "correo": row[1],
            "contrasenia": row[2]
        }
        usuarios.append(usuario)
    return usuarios