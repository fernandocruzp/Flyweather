from flask import Flask
def inicia():
    app = Flask(__name__, template_folder="template")
    app.config['SECRET_KEY']= 'secreto'

    from .vista import vista
    app.register_blueprint(vista,url_prefix='/')

    return app
