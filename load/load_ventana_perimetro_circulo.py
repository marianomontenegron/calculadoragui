from PyQt5 import QtWidgets, uic
from clases.calcular_circulo import CalcularCirculo

class VentanaCalcularCirculo(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_perimetro_circulo.ui", self)
        self.show()

        self.boton_calculo.clicked.connect(self.botonSumarClick)

    def botonSumarClick(self):
        r = int(self.edit_radio.text())
        calcularCirculo = CalcularCirculo(r)
        calcularCirculo.realizarCalculo()
        self.label_perimetro.setText(str(calcularCirculo.c))