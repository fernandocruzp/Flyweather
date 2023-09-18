from flask import Blueprint,render_template
from . import LlamaAPi

vista = Blueprint('vista',__name__)

@vista.route('/')
def inicio():
    return render_template("Inicio.html")

@vista.route('/ticket')
def ticket():   
    return render_template("Ticket.html")

@vista.route('/ciudad')
def ciudad():
    return render_template("CIudad.html")
