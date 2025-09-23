class Calculadora():
    def __init__ (self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
    def suma(self):
        return self.numero1 + self.numero2
        
    def resta(self):
        return self.numero1 - self.numero2
        
    def multiplicacion(self):
        return self.numero1*self.numero2
        
    def division(self):
        return self.numero1/self.numero2


prueba1 = Calculadora(1, 3)
prueba2 = Calculadora(1, 3)
prueba3 = Calculadora(1, 3)
prueba4 = Calculadora(1, 3)


print("La suma es", Calculadora.suma(prueba1))
print("La resta es", Calculadora.resta(prueba2))
print("La multiplicacion es", Calculadora.multiplicacion(prueba3))
print("La division es", Calculadora.division(prueba4))


    