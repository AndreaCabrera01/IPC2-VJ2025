from flask import Flask
from flask_cors import CORS
from news.routes import news_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(news_bp, url_prefix='/api/news')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=7000)