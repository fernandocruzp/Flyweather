import json
import requests
import datetime

llave="642a7ef347fb3a975cabd4001efd9afa"
def realizaBusqueda(lat,lon):
    respuesta = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={llave}")
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return "Error"
