class Litros():
    def __init__(self, Gal):
        self.Gal = Gal
        self.L = 0
        
    def leerDatos(self):
        self.Gal = int(input("Ingresa galones: "))

    def realizarCalculo(self):
        self.L = self.Gal*3.7854

    def mostrarresultado(self):  
        print(f"L = {self.L}L")