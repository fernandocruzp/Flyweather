import LlamaAPi
import csv

class Buscador:
    def __init__(self):
        self.cache={}
        self.cacheTicket={}

    def buscaTicket(self,ticket):
        if ticket in self.cacheTicket:
            return self.buscaCiudad(self.cacheTicket[ticket][0]), self.buscaCiudad(self.cacheTicket[ticket][1])

        with open("dataset2.csv", mode='r') as csvLector:
            csvCont = csv.DictReader(csvLector)
            for fila in csvCont:
                if fila['num_ticket'] == ticket:
                    self.cacheTicket[ticket]=[fila['origin'],fila['destination']]
                    return self.buscaCiudad(fila['origin']),self.buscaCiudad(fila['destination'])
            return None

    def buscaCiudad(self,nombre):
        if nombre in self.cache:
            return self.cache[nombre]

        clima= self.buscaClima(nombre)

        if clima:
            self.cache[nombre]=clima

        return clima

    def buscaClima(self,nombre):
        with open("dataset1.csv", mode='r') as csvLector:
            csvCont = csv.DictReader(csvLector)
            for fila in csvCont:
                if fila['origin'] == nombre:
                    return LlamaAPi.realizaBusqueda(fila['origin_latitude'],fila['origin_longitude'])
            return None