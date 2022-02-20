from app import app
import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
        # cria uma instancia do unittest, precisa do nome "setUp".
        self.app = app.test_client()

    def test_requisicao(self):
        # envia uma requisicao GET para a URL
        result = self.app.get('/index.html')

        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(result.status_code, 200) 

    def test_conteudo(self):
        # envia uma requisicao GET para a URL
        result = self.app.get('/index.hmtl') 

        # verifica o retorno do conteudo da pagina
        self.assertRegex(result.data.decode(), "Bem Vindo a página Guia do Dev")


if __name__ == "__main__":
    print ('INICIANDO OS TESTES')
    print('----------------------------------------------------------------------')
    unittest.main(verbosity=2)
    
