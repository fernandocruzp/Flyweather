import unittest
from main import app
from flask import Flask


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cliente = app.test_client()

    """
    Revisa que las rutas regresen la pagina correcta
    """
    def test_ticket(self):
        respuesta = self.cliente.post('/ticket', data={'ticket_id': 'kw9f0kwvZJmsukQy'})
        self.assertEqual(respuesta.status_code, 200)

    """
    Revisa que las rutas regresen la pagina correcta
    """
    def test_ciudad(self):
        respuesta = self.cliente.post('/ciudad', data={'ciudad': 'Monterrey'})
        self.assertEqual(respuesta.status_code, 200)

if __name__ == '__main__':
    unittest.main()
