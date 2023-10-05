import unittest
from website import LlamaAPi

class TestLlamaAPi(unittest.TestCase):

    
    def test_peticiones(self):
        """
    REVISAMOS QUE LA LLAMADA A LA API SE HAGA CORRECTAMENTE
    """
        resultado = LlamaAPi.realizaBusqueda("25.7785", "-100.107")
        assert  resultado["temp"] != None
        assert resultado["feels_like"] != None
        assert resultado["temp_min"] != None
        assert resultado["temp_max"] != None
        assert resultado["pressure"] != None
        assert resultado["humidity"] != None
        resultado = LlamaAPi.realizaBusqueda("DAS", "DSA")
        assert resultado== "Error"


if __name__ == '__main__':
    unittest.main()
