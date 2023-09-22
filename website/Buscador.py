from website import LlamaAPi
from website import matchingNames

import csv

class Buscador:
    def __init__(self):
        self.cache={}
        self.cacheTicket={}

    def buscaTicket(self, ticket):
        if ticket in self.cacheTicket:
            return self.buscaCiudad(self.cacheTicket[ticket][0]), self.buscaCiudad(self.cacheTicket[ticket][1])

        with open("website/datasets/dataset2.csv", mode='r') as csvLector:
            csvCont = csv.DictReader(csvLector)
            for fila in csvCont:
                if fila['num_ticket'] == ticket:
                    self.cacheTicket[ticket]=[fila['origin'],fila['destination']]
                    return self.buscaCiudad(fila['origin']),self.buscaCiudad(fila['destination'])
            return None, None

    def buscaCiudad(self, nombre):
        nombre.upper()
        if nombre in self.cache:
            return self.cache[nombre]
        else:
            nombre = matchingNames.matchea_ciudades(nombre)
            if nombre in self.cache:
                return self.cache[nombre]

        clima = self.buscaClima(nombre)

        if clima:
            self.cache[nombre]=clima
            n = {"Lugar": nombre}
            clima.update(n)
            return clima
        return None

    def buscaClima(self,nombre):
        with open("website/datasets/dataset1.csv", mode='r') as csvLector:
            csvCont = csv.DictReader(csvLector)
            for fila in csvCont:
                if fila['origin'] == nombre:
                    return LlamaAPi.realizaBusqueda(fila['origin_latitude'],fila['origin_longitude'])
                elif fila['destination'] == nombre:
                    return LlamaAPi.realizaBusqueda(fila['destination_latitude'], fila['destination_longitude'])
            return None