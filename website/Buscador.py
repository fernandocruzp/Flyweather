from website import LlamaAPi
from website import matchingNames
import csv

class Buscador:
    def __init__(self):
        """
        Inicializa una instancia de la clase Buscador.
        Crea cachés para resultados de búsqueda de clima por nombre de ciudad y número de ticket.
        """
        self.cache = {}  # Caché para almacenar resultados de búsqueda de clima por nombre de ciudad
        self.cacheTicket = {}  # Caché para almacenar resultados de búsqueda de clima por número de ticket

    def buscaTicket(self, ticket):
        """
        Busca un ticket en un archivo CSV y devuelve el clima de la ciudad de origen y destino asociada al ticket.
        
        Args:
            ticket (str): Número de ticket que se desea buscar.

        Returns:
            tuple: Una tupla que contiene el clima de la ciudad de origen y destino (en ese orden).
        """
        if ticket in self.cacheTicket:
            return self.buscaCiudad(self.cacheTicket[ticket][0]), self.buscaCiudad(self.cacheTicket[ticket][1])

        with open("website/datasets/dataset2.csv", mode='r') as csvLector:
            csvCont = csv.DictReader(csvLector)
            for fila in csvCont:
                if fila['num_ticket'] == ticket:
                    self.cacheTicket[ticket] = [fila['origin'], fila['destination']]
                    return self.buscaCiudad(fila['origin']), self.buscaCiudad(fila['destination'])
            return None, None

    def buscaCiudad(self, nombre):
        """
        Busca una ciudad en un archivo CSV y devuelve el clima asociado a la ciudad.
        
        Args:
            nombre (str): Nombre de la ciudad que se desea buscar.

        Returns:
            dict: Un diccionario que contiene información sobre el clima de la ciudad.
        """
        nombre = nombre.upper()  # Convertimos el nombre a mayúsculas

        if nombre in self.cache:
            return self.cache[nombre]
        else:
            nombre = matchingNames.matchea_ciudades(nombre)
            if nombre in self.cache:
                return self.cache[nombre]

        clima = self.buscaClima(nombre)
       
        if clima:
            self.cache[nombre] = clima
            nombreAgrega = {"Lugar": nombre}
            clima.update(nombreAgrega)
            return clima
        return None

    def buscaClima(self, nombre):
        """
        Busca el clima de una ciudad en un archivo CSV y realiza una llamada a la API para obtener el clima actual.
        
        Args:
            nombre (str): Nombre de la ciudad de la que se desea obtener el clima.

        Returns:
            dict: Un diccionario que contiene información sobre el clima de la ciudad.
        """
        with open("website/datasets/dataset1.csv", mode='r') as csvLector:
            csvCont = csv.DictReader(csvLector)
            for fila in csvCont:
                if fila['origin'] == nombre:
                    return LlamaAPi.realizaBusqueda(fila['origin_latitude'], fila['origin_longitude'])
                elif fila['destination'] == nombre:
                    return LlamaAPi.realizaBusqueda(fila['destination_latitude'], fila['destination_longitude'])
            return None
