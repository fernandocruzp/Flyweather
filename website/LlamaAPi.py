import requests
llave="da11b5bd3b772efa31a4aff7e524e16b"
#Módulo para realizar llamada de API OPENWEATHERMAP
def realizaBusqueda(lat,lon):
    respuesta = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={llave}")
    if respuesta.status_code == 200:
        #Regresamos solamente la parte main de la respuesta del json
        return respuesta.json()["main"]
    else:
        return "Error"

