from flask import Blueprint, jsonify, request
from .models import Noticia

news_bp = Blueprint('news', __name__)

noticias = []
idContador = 1

@news_bp.route('/', methods=['GET'])
def get_all_news():
    return jsonify([noticia.to_dict() for noticia in noticias]), 200

# Registrar noticia nueva:
@news_bp.route('/', methods=['POST'])
def create_news():
    global idContador
    data = request.get_json()
    if not data or 'titulo' not in data or 'contenido' not in data:
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    
    nueva_noticia = Noticia(idContador, data['titulo'], data['contenido'])
    noticias.append(nueva_noticia)
    idContador += 1
    return jsonify({'message': 'Noticia agregada'}), 201

# Update a la noticia:
@news_bp.route('/<int:news_id>', methods=['PUT'])
def update_news(news_id):
    data = request.get_json()
    noticia = next((n for n in noticias if n.id == news_id), None)
    if not noticia:
        return jsonify({'error': 'Noticia no encontrada'}), 404
    
    noticia.titulo = data.get('titulo', noticia.titulo)
    noticia.contenido = data.get('contenido', noticia.contenido)
    return jsonify({'message': 'Noticia actualizada correctamente'}), 200

# Delete de la noticia:
@news_bp.route('/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    global noticias
    noticia = next((n for n in noticias if n.id == news_id), None)
    if not noticia:
        return jsonify({'error': 'Noticia no encontrada'}), 404
    
    noticias = [n for n in noticias if n.id != news_id]
    return jsonify({'message': 'Noticia eliminada correctamente'}), 200