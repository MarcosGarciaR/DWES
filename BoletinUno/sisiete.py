class FiguraGeometrica():
    def __init__(self, ancho=0, altura=0):
        self.ancho = ancho
        self.altura = altura
        
    def calcularArea(self):
        return 

class Rectangulo(FiguraGeometrica):
    def __init__(self):
        super().__init__(ancho, altura)
    
    def calcularArea(self):
        return self.ancho*self.altura
    
class Triangulo(FiguraGeometrica):
    def __init__(self):
        super().__init__(ancho, altura)
        
    def calcularArea(self):
        return (self.ancho*self.altura) / 2

figura1 = Rectangulo(10, 5)
figura2 = Triangulo(10, 5)