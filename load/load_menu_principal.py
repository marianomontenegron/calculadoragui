from PyQt5 import QtWidgets, uic
from load.load_ventana_calculadora import VentanaCalculadora
from load.load_ventana_calcular_Gal_a_L import VentanaCalcularL
from load.load_ventana_millas_a_Km import VentanaCalcularKm
from load.load_ventana_perimetro_circulo import VentanaCalcularCirculo

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui", self)
        self.showMaximized()

        self.actionCalculadora.triggered.connect(self.ingresarCalculadora)
        self.actionCalcular_Galones_a_Litros.triggered.connect(self.ingresarCalcular_Galones_a_Litros)
        self.actionCalcular_de_millas_a_Km.triggered.connect(self.ingresarCalcular_de_millas_a_Km)
        self.actionCalcular_per_metro_de_c_rculo.triggered.connect(self.ingresarCalcular_per_metro_de_c_rculo)
        self.actionSalir.triggered.connect(self.salir)

    def ingresarCalculadora(self):
        calculadora = VentanaCalculadora()
        calculadora.exec()

    def ingresarCalcular_Galones_a_Litros(self):
        calcularL = VentanaCalcularL()
        calcularL.exec()

    def ingresarCalcular_de_millas_a_Km(self):
        calcularKm = VentanaCalcularKm()
        calcularKm.exec()

    def ingresarCalcular_per_metro_de_c_rculo(self):
        calcularCirculo = VentanaCalcularCirculo()
        calcularCirculo.exec()

    def salir(self):
        self.close()
