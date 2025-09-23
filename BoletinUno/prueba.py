import unittest

from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        print("Realizando prueba")
        self.calculadora = Calculadora(8, 2)
        
    def test_suma(self):
        print("prueba de suma correcta")
        calculadora=Calculadora(8,2)
        self.assertEqual(calculadora.suma(), 10, "La suma no es correcta")
        
    def test_suma_erronea(self):
        print("Prueba de suma incorrecta")
        calculadora=Calculadora(8,2)
        self.assertNotEqual(calculadora.suma(), 11, "La suma es correcta, programa erroneo")

    def test_resta(self):
        self.assertEqual(self.calculadora.resta(), 6, "Resta mal hecha")
        
    def test_resta_erronea(self):
        self.assertNotEqual(self.calculadora.resta(), 7, "Resta mal hecha")
        
    def test_multiplicacion(self):
        self.assertEqual(self.calculadora.multiplicacion(), 16, "La multiplicacion está mal hecha")
        
    def test_multiplicacion_erronea(self):
        self.assertNotEqual(self.calculadora.multiplicacion(), 15, "La multiplicacion está mal hecha")
        
    def test_division(self):
        self.assertEqual(self.calculadora.division(), 4, "La division no es correcta")
        
    def test_division_erronea(self):
        self.assertNotEqual(self.calculadora.division(), 3, "La division está mal hecha")
    
    def tearDown(self):
        print("FIN Prueba")


if __name__ == '__main__':
    unittest.main()

