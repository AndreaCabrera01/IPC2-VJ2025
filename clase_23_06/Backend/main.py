from flask import Flask, request, jsonify
from flask_cors import CORS

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
    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')


# pip install flask flask-cors