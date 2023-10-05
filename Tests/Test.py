import unittest
from main import app
from flask import Flask

class MyTestCase(unittest.TestCase):
    """
    Clase de pruebas para la aplicación Flask 'app'.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        self.cliente = app.test_client()

    def test_ticket(self):
        """
        Prueba la ruta '/ticket' de la aplicación.
        Realiza una solicitud POST con un ticket válido y verifica el código de estado de la respuesta.
        """
        respuesta = self.cliente.post('/ticket', data={'ticket_id': 'kw9f0kwvZJmsukQy'})
        self.assertEqual(respuesta.status_code, 200)

    def test_ciudad(self):
        """
        Prueba la ruta '/ciudad' de la aplicación.
        Realiza una solicitud POST con el nombre de una ciudad y verifica el código de estado de la respuesta.
        """
        respuesta = self.cliente.post('/ciudad', data={'ciudad': 'Monterrey'})
        self.assertEqual(respuesta.status_code, 200)

if __name__ == '__main__':
    unittest.main()
