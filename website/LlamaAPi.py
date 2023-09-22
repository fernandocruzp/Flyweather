import json
import requests
import datetime

llave="da11b5bd3b772efa31a4aff7e524e16b"
def realizaBusqueda(lat,lon):
    respuesta = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={llave}")
    if respuesta.status_code == 200:
        return respuesta.json()["main"]
    else:
        return "Error"

