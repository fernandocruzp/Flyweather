from website import LlamaAPi
from website import matchingNames

import csv

class Buscador:
    def __init__(self):
        self.cache={}
        self.cacheTicket={}

#Busca ticket en archivo csv y regresa clima de ciudad de origen y destino
    def buscaTicket(self, ticket):
        #Revisa caché para evitar búsquedas de más
        if ticket in self.cacheTicket:
            return self.buscaCiudad(self.cacheTicket[ticket][0]), self.buscaCiudad(self.cacheTicket[ticket][1])

#Revisamos dataset2 para buscar ticket
        with open("website/datasets/dataset2.csv", mode='r') as csvLector:
            csvCont = csv.DictReader(csvLector)
            for fila in csvCont:
                if fila['num_ticket'] == ticket:
                    #Agregamos ticket al caché
                    self.cacheTicket[ticket]=[fila['origin'],fila['destination']]
                    return self.buscaCiudad(fila['origin']),self.buscaCiudad(fila['destination'])
            return None, None

#Revisamos ciudad en archivo csv y regresa clima de ciudad
    def buscaCiudad(self, nombre):
        nombre.upper()
        #Revisamos cache
        if nombre in self.cache:
            return self.cache[nombre]
        else:
            #Utilizamos módulo mathcinNmes para encontrar la ciudad con el nombre más parecido al introducido
            nombre = matchingNames.matchea_ciudades(nombre)
            if nombre in self.cache:
                return self.cache[nombre]

        clima = self.buscaClima(nombre)
        #Si la llamada a nuestra API es diferente a error
        if clima:
            self.cache[nombre]=clima
            n = {"Lugar": nombre}
            clima.update(n)
            return clima
        return None

    def buscaClima(self,nombre):
        #Buscamos ciudad en archivo csv
        with open("website/datasets/dataset1.csv", mode='r') as csvLector:
            csvCont = csv.DictReader(csvLector)
            for fila in csvCont:
                if fila['origin'] == nombre:
                    #Realizamos llamada a la API
                    return LlamaAPi.realizaBusqueda(fila['origin_latitude'],fila['origin_longitude'])
                elif fila['destination'] == nombre:
                    # Realizamos llamada a la API
                    return LlamaAPi.realizaBusqueda(fila['destination_latitude'], fila['destination_longitude'])
            return None