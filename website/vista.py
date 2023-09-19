from flask import Blueprint,render_template,request

from website import Buscador

vista = Blueprint('vista',__name__)

buscador = Buscador.Buscador()

@vista.route('/')
def inicio():
    return render_template("Index.html")

@vista.route('/ticket', methods=["GET","POST"])
def ticket():
    if request.method == "POST":
        ticket_id = request.form.get("ticket_id")
        print(ticket_id)
        ciudadA, ciudadB = buscador.buscaTicket(ticket_id)
        return render_template("Ticket.html", tickets=[ciudadA,ciudadB])
    return render_template("Ticket.html")

@vista.route('/ciudad', methods=["GET","POST"])
def ciudad():
    if request.method == "POST":
        ciudad = request.form.get("ciudad")
        print(ciudad)
        ciudadA= buscador.buscaCiudad(ciudad)
        return render_template("CIudad.html", tickets=[ciudadA])
    return render_template("CIudad.html")
