from flask import Blueprint, render_template, request
from website import Buscador

# Crear un objeto Blueprint llamado 'vista'
vista = Blueprint('vista', __name__)

# Crear una instancia del Buscador
buscador = Buscador.Buscador()

@vista.route('/')
def inicio():
    """
    Ruta de inicio que renderiza la página Index.html.
    """
    return render_template("Index.html")

@vista.route('/ticket', methods=["GET","POST"])
def ticket():
    """
    Ruta que maneja la búsqueda de información sobre un ticket.
    Permite tanto solicitudes GET como POST.

    Si es una solicitud POST, busca información del ticket y muestra los resultados en Ticket.html.
    Si es una solicitud GET, muestra un formulario en Ticket.html.

    Returns:
        render_template: Una plantilla HTML renderizada con los resultados o el formulario de búsqueda.
    """
    if request.method == "POST":
        ticket_id = request.form.get("ticket_id")
        ciudadA, ciudadB = buscador.buscaTicket(ticket_id)
        return render_template("Ticket.html", tickets=[ciudadA, ciudadB])
    return render_template("Ticket.html", tickets=[None, None])

@vista.route('/ciudad', methods=["GET","POST"])
def ciudad():
    """
    Ruta que maneja la búsqueda de información sobre una ciudad.
    Permite tanto solicitudes GET como POST.

    Si es una solicitud POST, busca información de la ciudad y muestra los resultados en Ciudad.html.
    Si es una solicitud GET, muestra un formulario en Ciudad.html.

    Returns:
        render_template: Una plantilla HTML renderizada con los resultados o el formulario de búsqueda.
    """
    if request.method == "POST":
        ciudad = request.form.get("ciudad")
        ciudadA = buscador.buscaCiudad(ciudad)
        return render_template("CIudad.html", tickets=[ciudadA])
    return render_template("CIudad.html")

@vista.errorhandler(500)
def internal_errorC(e):
    """
    Manejador de errores para errores internos del servidor (código 500).
    Renderiza la página 500.html en caso de un error interno.

    Args:
        e: El error que se ha producido.

    Returns:
        render_template: Una plantilla HTML renderizada de la página de error 500.
    """
    return render_template('500.html'), 500

@vista.errorhandler(400)
def internal_errorT(e):
    """
    Manejador de errores para errores internos del servidor (código 500).
    Renderiza la página 500.html en caso de un error interno.

    Args:
        e: El error que se ha producido.

    Returns:
        render_template: Una plantilla HTML renderizada de la página de error 500.
    """
    return render_template('400.html'), 400

