from flask import Flask, jsonify #def
from conexion import get_usuarios

app = Flask(__name__) #nombre del archivo que se va ejecutar def

@app.route("/")

def hi():
    return "<h1>wola<h1>"

# @app.route("/usuarios/<string:nombre>") #en plural
# def usuarios(nombre):
#     return "hola %s" % nombre 

@app.route("/api/v1/usuarios")
def usuarios():
    usuarios_lista = get_usuarios()
    # usuario_dict = {
    #     "id": 10,
    #     "correo": "ximena@correo.com",
    #     "contrasenia": "123"
    # }

    # usuarios_lista.append(usuario_dict)
    
    return jsonify(usuarios_lista)

app.run()