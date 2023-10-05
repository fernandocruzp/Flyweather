import requests

def realizaBusqueda(lat, lon):
    """
    Realiza una búsqueda del clima actual utilizando coordenadas de latitud y longitud para realizar llamada a la api de OpenWeather.
    
    Args:
        lat (float): Latitud de la ubicación.
        lon (float): Longitud de la ubicación.

    Returns:
        dict or str: Un diccionario que contiene información sobre el clima actual si la solicitud es exitosa.
                     En caso de error en la solicitud, devuelve un mensaje de error.
    """
    respuesta = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={'da11b5bd3b772efa31a4aff7e524e16b'}")
    
    if respuesta.status_code == 200:
        clima = respuesta.json()["main"]
        n = {"clima": respuesta.json()["weather"][0]["main"]}
        clima.update(n)
        return clima
    else:
        return "Error en la solicitud de clima"

