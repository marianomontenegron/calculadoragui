from PyQt5 import QtWidgets, uic
from clases.calcular_galones_a_litros import Litros

class VentanaCalcularL(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_calcular_Gal_a_L.ui", self)
        self.show()

        self.boton_litros.clicked.connect(self.botonSumarClick)

    def botonSumarClick(self):
        Gal = int(self.edit_galones.text())
        calcularL = Litros(Gal)
        calcularL.realizarCalculo()
        self.label_resultadoL.setText(str(calcularL.L))