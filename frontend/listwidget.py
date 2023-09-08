from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from backend import *

class ListWidget(QWidget):

    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("ListWidget.ui", self)

        self.nombre_list.setText(cs.curves[-1].name)
        #self.color.setStyleSheet("background-color:" + color)
        self.visibilidad_list.clicked.connect(self.goto_visibilidad)
        self.color_list.clicked.connect(self.goto_color)
        self.datos_list.clicked.connect(self.goto_datos)
        self.borrar_list.clicked.connect(self.goto_borrar)

    def goto_visibilidad (self):
        cs.curves[-1].change_visibility()


    def goto_color(self):
        print("messi")

    def goto_datos(self):
        print("messi")

    def goto_borrar(self):
        print("messi")



