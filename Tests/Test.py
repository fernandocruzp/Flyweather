import unittest
from website import vista
from flask import Flask

class MyTestCase(unittest.TestCase):

    def setUp(self) :
        self.proy = Flask(__name__)
        self.proy.register_blueprint(vista)

        self.proy.config['TESTING'] =True
        self.cliente = self.proy.test_client()


    def test_ticket(self):
        respuesta = self.cliente.post('/ticket', data={'ticket_id': 'kw9f0kwvZJmsukQy'})



if __name__ == '__main__':
    unittest.main()
