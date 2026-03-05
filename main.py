from load.load_ventana_calculadora import VentanaCalculadora
from load.load_ventana_millas_a_Km import VentanaCalcularKm
from load.load_ventana_calcular_Gal_a_L import VentanaCalcularL
from load.load_ventana_perimetro_circulo import VentanaCalcularCirculo
from PyQt5 import QtWidgets
import sys



def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaCalcularCirculo()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    