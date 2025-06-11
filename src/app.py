import sys
from PySide6 import QtWidgets
from calculator import Calculator

class CalculatorApp(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationName("InterCalc")
        self.window = Calculator()
        self.window.show()