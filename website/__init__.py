from flask import Flask

def inicia():
    """
    Inicializa una aplicación Flask y configura rutas y configuraciones básicas.
    
    Returns:
        Flask: La instancia de la aplicación Flask configurada.
    """
    
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__, template_folder="template")

    # Configura una clave secreta para la aplicación (puede ser cualquier valor secreto)
    app.config['SECRET_KEY'] = 'secreto'

    # Importa el módulo 'vista' y registra el Blueprint para las rutas
    from .vista import vista
    app.register_blueprint(vista, url_prefix='/')

    return app

