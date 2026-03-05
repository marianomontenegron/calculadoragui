import math
class CalcularCirculo():
    def __init__(self, r):
        self.r = r
        self.c = 0
        
    def leerDatos(self):
        self.r = int(input("Ingresa r: "))
        
    def realizarCalculo(self):
        self.c = 2*math.pi*self.r

    def mostrarresultado(self):   
        print("c = ",round(self.c,2))