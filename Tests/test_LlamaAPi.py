import unittest
import sys
sys.path.insert(0, '..')
#sys.path.append('..')
#import website
from website import LlamaAPi
#from LlamaAPi import realizaBusqueda


class TestLlamaAPi(unittest.TestCase):

    def test_peticiones(self):
        resultado = LlamaAPi.realizaBusqueda("25.7785", "-100.107")
        assert resultado.status_code == 200
        #assert  nombreCiudad == 'Monterrey'
        #assert nombrePais == 'MX'

    """
    def test_realizaBusqueda(self):
        nombreCiudad = resultado["name"]
        nombrePais = resultado['sys']['country']
    
    """
if __name__ == '__main__':
    unittest.main()
