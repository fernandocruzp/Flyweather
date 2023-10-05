import unittest
from website import Buscador
from website import LlamaAPi

class TestBuscador(unittest.TestCase):
    """
    Pruebas para la clase Buscador.
    """

    def test_buscaTicket(self):
        """
        Prueba el método buscaTicket.
        """
        origen = LlamaAPi.realizaBusqueda("19.4363", "-99.0721")
        destino = LlamaAPi.realizaBusqueda("25.7785", "-100.107")
        buscador = Buscador.Buscador()
        origen2, destino2 = buscador.buscaTicket("PheImPzc32OUR8pL")
        self.assertEqual(origen, origen2)
        self.assertEqual(destino, destino2)

    def test_Cache(self):
        """
        Prueba la funcionalidad de la caché.
        """
        buscador = Buscador.Buscador()
        # Verifica que la caché esté vacía inicialmente
        self.assertEqual(len(buscador.cache), 0)
        # Realiza una búsqueda para llenar la caché
        resultado = buscador.buscaCiudad('MTY')
        # Verifica que la caché tenga un elemento después de la búsqueda
        self.assertEqual(len(buscador.cache), 1)
        # Realiza otra búsqueda con la misma ciudad, la caché no debe cambiar
        resultado = buscador.buscaCiudad('MTY')
        self.assertEqual(len(buscador.cache), 1)
        # Realiza una búsqueda de ticket para llenar la caché de tickets
        a, b = buscador.buscaTicket("PheImPzc32OUR8pL")
        # Verifica que la caché de tickets tenga un elemento
        self.assertEqual(len(buscador.cacheTicket), 1)

    def test_buscaClima(self):
        """
        Prueba el método buscaClima.
        """
        buscador = Buscador.Buscador()
        clima_MTY = LlamaAPi.realizaBusqueda("25.7785", "-100.107")
        resultado = buscador.buscaClima('MTY')
        climaAPi = clima_MTY['temp']
        climaClima = resultado['temp']
        self.assertEqual(climaAPi, climaClima)

if __name__ == '__main__':
    unittest.main()
