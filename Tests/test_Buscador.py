import unittest
from website import Buscador
from website import LlamaAPi


class TestBuscador(unittest.TestCase):

    def test_buscaTicket(self):
        origen = LlamaAPi.realizaBusqueda("19.4363", "-99.0721")
        destino = LlamaAPi.realizaBusqueda("25.7785", "-100.107")
        conTicket = Buscador.buscaTicket("PheImPzc32OUR8pL")
        #como buscas en los dos


    def test_buscaCiudad(self):
        return 0

    def test_buscaClima(self):
        clima_MTY = LlamaAPi.realizaBusqueda("25.7785", "-100.107")
        resultado = Buscador.buscaClima('MTY')
        ciudadAPi = clima_MTY['name']
        ciudadClima = resultado['name']
        climaAPi = clima_MTY['temp']
        climaClima = resultado['temp']
        assert ciudadAPi == ciudadClima
        assert climaAPi == climaClima


if __name__ == '__main__':
    unittest.main()
