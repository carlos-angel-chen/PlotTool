from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import *

class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        #ToolBar1.addWidget(NavigationToolbar(self.canvas, self))

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

    def make_ToolBar (self, layout):
        layout.addWidget(NavigationToolbar(self.canvas, self))

class MplWidget2(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        #vertical_layout.addWidget(NavigationToolbar(self.canvas, self))

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

    def make_ToolBar (self, layout):
        layout.addWidget(NavigationToolbar(self.canvas, self))


class MplWidget3(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        #vertical_layout.addWidget(NavigationToolbar(self.canvas, self))

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

    def make_ToolBar (self, layout):
        layout.addWidget(NavigationToolbar(self.canvas, self))

