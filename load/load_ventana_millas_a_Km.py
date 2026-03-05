from PyQt5 import QtWidgets, uic
from clases.calcularKm import CalcularKm

class VentanaCalcularKm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_millas_a_Km.ui", self)
        self.show()

        self.boton_Calcular.clicked.connect(self.botonSumarClick)

    def botonSumarClick(self):
        mill = int(self.edit_millas.text())
        calcularKm = CalcularKm(mill)
        calcularKm.realizarCalculo()
        self.label_resultadokm.setText(str(calcularKm.km))