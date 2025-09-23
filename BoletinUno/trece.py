class Estudiante ():
    
    def __init__(self,nombre = "", edad =0, curso=""):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
    
    def __str__(self):
        return f"{self.nombre} {self.edad} {self.curso}"

est1 = Estudiante("Marcos", 19, "2ºDAW")
est2 = Estudiante("Gamez", 25, "2ºDAW")
est3 = Estudiante("Varo", 18, "2ºDAM")
        
lista = [est1, est2, est3]

for estudiante in lista:
    print(estudiante)

print("FIN lista")

