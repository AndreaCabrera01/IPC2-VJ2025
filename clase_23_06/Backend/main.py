from flask import Flask, request, jsonify
from flask_cors import CORS
from xml.etree import ElementTree as ET
from User import User
from Animal import Animal
from xml.dom import minidom

app = Flask(__name__)
CORS(app)

users = {
    "admin" : {
        "id": 1,
        "password": "1234",
        "role": 0
    }
}

logueado_actual = ''
listadoUsuarios = []
listadoAnimales = []


@app.route('/login', methods=['POST'])
def login():
    global logueado_actual

    if logueado_actual:
        return jsonify({"error": "Ya hay un usuario logueado"}), 400
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Hacen falta datos"}), 400
    
    if username == "admin" and password == users["admin"]["password"]:
        logueado_actual = username
        return jsonify({"message": "Login exitoso", "role": 0}), 200
    else:
        for user in listadoUsuarios:
            if user.username == username and user.password == password:
                logueado_actual = username
                return jsonify({"message": "Login Exitoso", "role": 1}), 200
            
    return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route('/obtener_logueado', methods=['GET'])
def obtener_logueado():
    if logueado_actual:
        return jsonify({"logueado": logueado_actual}), 200
    return jsonify({"error": "No hay usuario logueado"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    global logueado_actual
    logueado_actual = ''
    return jsonify({"message": "Logout exitoso"}), 200


@app.route('/procesarXML', methods=['POST'])
def procesar_xml():
    if not logueado_actual == 'admin':
        return jsonify({"error": "No tienes permisos para procesar XML"}), 403
    
    print("XML QUE EL FRONT NOS ENVÍA")
    xml_file = request.data
    
    decodificar = xml_file.decode('utf-8')

    root = ET.fromstring(decodificar)

    contadorUsers = 0
    contadorAnimales = 0

    global listadoUsuarios, listadoAnimales

    usuarios_xml = root.find('usuarios')
    if usuarios_xml is not None:
        for u in usuarios_xml.findall('usuario'):
            username = u.attrib.get('user')
            password = u.attrib.get('password')
            if username and password:
                usuario = User(username, password)
                listadoUsuarios.append(usuario)
                contadorUsers += 1

    mascotas_xml = root.find('mascotas')
    if mascotas_xml is not None:
        for m in mascotas_xml.findall('mascota'):
            tipo = m.attrib.get('tipo')
            edad = m.attrib.get('edad')
            cuidador = m.attrib.get('cuidador')
            nombre = m.text.strip() if m.text else ''
            if tipo and nombre:
                animal = Animal(nombre, tipo, edad, cuidador)
                listadoAnimales.append(animal)
                contadorAnimales += 1

    
    # Creando XML de respuesta
    response_root = ET.Element('respuesta')
    ET.SubElement(response_root, 'usuarios_procesados').text = str(contadorUsers)
    ET.SubElement(response_root, 'animales_procesados').text = str(contadorAnimales)

    mensaje_xml = ET.tostring(response_root, encoding='utf-8', xml_declaration=True)

    # prettify the XML response
    parsed_xml = minidom.parseString(mensaje_xml)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")    

    return jsonify({"message": pretty_xml}), 200

@app.route('/verUsuarios', methods=['GET'])
def ver_usuarios():
    if not logueado_actual == 'admin':
        return jsonify({"error": "No tienes permisos para ver usuarios"}), 403
    
    usuarios = [{"username": user.username, "password": user.password} for user in listadoUsuarios]
    return jsonify({"usuarios": usuarios}), 200

@app.route('/verAnimales', methods=['GET'])
def ver_animales():
    if not logueado_actual == 'admin':
        return jsonify({"error": "No tienes permisos para ver animales"}), 403
    
    animales = [{"nombre": animal.nombre, "tipo": animal.tipo} for animal in listadoAnimales]
    return jsonify({"animales": animales}), 200

@app.route('/verMisAnimales/<cuidador>', methods=['GET'])
def ver_mis_animales(cuidador):
    if not logueado_actual:
        return jsonify({'error': 'No hay usuario logueado'})

    animales =[animal for animal in listadoAnimales if animal.cuidador == cuidador]
    if not animales:
        return jsonify({"error": "No se encontraron animales para el cuidador especificado"}), 404
    
    animales_info = [{"nombre": animal.nombre, "tipo": animal.tipo, "edad": animal.edad} for animal in animales]
    return jsonify({"animales": animales_info}), 200


@app.route('/reporteAnimales/<cuidador>/<top>', methods=['GET'])
def reporte_animales(cuidador, top):
    if not logueado_actual:
        return jsonify({"error": "No hay usuario logueado"}), 401
    
    try:
        top = int(top)
    except ValueError:
        return jsonify({"error": "El parámetro 'top' debe ser un número entero"}), 400

    animales = [animal for animal in listadoAnimales if animal.cuidador == cuidador]
    if not animales:
        return jsonify({"error": "No se encontraron animales para el cuidador especificado"}), 404

    # Ordenar los animales por edad (de mayor a menor)
    animales_ordenados = sorted(animales, key=lambda x: x.edad, reverse=True)

    # LIMITAR:.
    animales_top = animales_ordenados
    if top >0:
        animales_top = animales_ordenados[:top]

    # Obtener la información por medio de 2 listas, una para los nombres y otra para los valores:
    animalesNombres = [animal.nombre for animal in animales_top]
    animalesEdades = [animal.edad for animal in animales_top]

    animales_info = {
        "nombres": animalesNombres,
        "edades": animalesEdades
    }

    return jsonify(animales_info), 200


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')


# pip install flask flask-cors