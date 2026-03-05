class CalcularKm(object):
    def __init__(self, mill):
        self.mill = mill
        self.km = 0
        
    def leerDatos(self):
        self.mill = int(input("Ingresa millas: "))

    def realizarCalculo(self):   
        self.km = self.mill*1.609344
    
    def mostrarresultado(self): 
        print(f"km = {self.km}km")