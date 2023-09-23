import unittest
from website import Buscador
from website import LlamaAPi


class TestBuscador(unittest.TestCase):


    #TEST QUE VERIFICA SI SE BUSCA BIEN EL TICKET
    def test_buscaTicket(self):
        origen = LlamaAPi.realizaBusqueda("19.4363", "-99.0721")
        n = {"Lugar": "MEX"}
        origen.update(n)
        destino = LlamaAPi.realizaBusqueda("25.7785", "-100.107")
        m={"Lugar": "MTY"}
        destino.update(m)
        buscador = Buscador.Buscador()
        origen2,destino2 = buscador.buscaTicket("PheImPzc32OUR8pL")
        self.assertEquals(origen,origen2)
        self.assertEquals(destino,destino2)

#REVISA QUE EL CACHE FUNCIONA
    def test_Cache(self):
        buscador = Buscador.Buscador()
        #CACHE DEBE ESTAR VACÍO
        self.assertEquals(len(buscador.cache),0)
        resultado = buscador.buscaCiudad('MTY')
        self.assertEquals(len(buscador.cache), 1)
        #OBTIENE CIUDAD DIRECTAMENTE DEL CACHE
        resultado=buscador.buscaCiudad('MTY')
        self.assertEquals(len(buscador.cache),1)
        a,b=buscador.buscaTicket("PheImPzc32OUR8pL")
        self.assertEquals(len(buscador.cache), 2)
        #REVISAMOS CACHETICKET
        self.assertEquals(len(buscador.cacheTicket),1)

#VERIFICAMOS QUE FUNCIONE EL MÉTODO BUSCARCIUDAD()
    def test_buscaClima(self):
        buscador = Buscador.Buscador()
        clima_MTY = LlamaAPi.realizaBusqueda("25.7785", "-100.107")
        resultado = buscador.buscaClima('MTY')
        climaAPi = clima_MTY['temp']
        climaClima = resultado['temp']
        assert climaAPi == climaClima


if __name__ == '__main__':
    unittest.main()
