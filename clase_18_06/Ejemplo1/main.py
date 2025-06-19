from flask import Flask, jsonify, request
from flask_cors import CORS

# Flask app:
app = Flask(__name__)
CORS(app)

listadoUsuarios = []

# Clases:
class Usuario:
    def __init__(self, usuario, fechaCreacion, password, rol):
        self.usuario = usuario
        self.fechaCreacion = fechaCreacion
        self.password = password
        self.rol = rol
        self.id = None

@app.route('/')
def index():
    return 'Mi server si está corriendo.'

@app.route('/ping', methods=['GET'])
def p():
    return jsonify({'message': 'pong'})

# CREAR USUARIO:
@app.route('/api/usuarios', methods=['POST'])
def post_usuario():
    data = request.get_json()

    # TIPO DE JSON A ENVIAR:
    # {
    #     'usuario': 'nombre_usuario',
    #     'fechaCreacion': '18-06-2025',
    #     'password': 'contrasenia123',
    #     'rol': 1
    # }

    if not data or 'usuario' not in data or 'fechaCreacion' not in data or 'password' not in data or 'rol' not in data:
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    
    nuevo_usuario = Usuario(
        usuario=data['usuario'], 
        fechaCreacion=data['fechaCreacion'], 
        password=data['password'], 
        rol=data['rol'],
    )

    nuevo_usuario.id = len(listadoUsuarios) + 1

    listadoUsuarios.append(nuevo_usuario)
    return jsonify({'message': 'Usuario creado exitosamente'}), 201

# VER USUARIOS:
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios_list = []
    for usuario in listadoUsuarios:
        usuarios_list.append({
            'usuario': usuario.usuario,
            'fechaCreacion': usuario.fechaCreacion,
            'password': usuario.password,
            'rol': usuario.rol,
            'id': usuario.id
        })

    return jsonify(usuarios_list), 200

# LIMPIAR DATOS:
@app.route('/api/usuarios/limpiar', methods=['DELETE'])
def limpiar_usuarios():
    global listadoUsuarios
    listadoUsuarios = []
    return jsonify({'message': 'Listado de usuarios exitosamente limpiados.'}), 200

# ELIMINAR USUARIO ESPECÍFICO:
@app.route('/api/usuarios/eliminar/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    global listadoUsuarios

    for usuario in listadoUsuarios:
        if usuario.id == id:
            listadoUsuarios.remove(usuario)
            return jsonify({'message': 'Usuario eliminado correctamente.'}), 200
    
    return jsonify({'error': 'Usuario no encontrado'}), 404

@app.route('/api/usuarios/getUser/<int:id>', methods=['GET'])
def get_usuario(id):
    for usuario in listadoUsuarios:
        if usuario.id == id:
            return jsonify({
                'usuario': usuario.usuario,
                'fechaCreacion': usuario.fechaCreacion,
                'rol': usuario.rol,
                'id': usuario.id
            }), 200
    
    return jsonify({'error': 'Usuario no encontrado'}), 404

@app.route('/api/usuarios/updatePassword', methods=['PUT'])
def update_password():
    data = request.get_json()

    # TIPO DE JSON A ENVIAR:
    # {
    #     'newPassword': nuevaPassword,
    #     'id': 1
    # }

    if not data or 'id' not in data or 'newPassword' not in data:
        return jsonify({'error': 'Faltan campos en el JSON'}), 400

    for usuario in listadoUsuarios:
        if usuario.id == data['id']:
            usuario.password = data['newPassword']
            return jsonify({'message': 'Contraseña actualizada correctamente'}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
