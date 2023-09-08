import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from frecspace import *
from timespace import *
import numpy as np


#Windows
class Input_Teorico_Window(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi("input_teorico.ui", self)
        self.setWindowTitle("Input Teórico")

        self.show()
        self.line_ecuacion.hide()
        self.ok_teorico_pushButton.clicked.connect(self.display_ok)
        self.ecuacion_teorico_pushButton.clicked.connect(self.display_ecuacion)
        self.cancel_teorico_pushButton.clicked.connect(self.close)


    def display_ok(self):
        self.nombre_input = self.nombre_graph_teorico.text()
        numerador_input = self.numerador_teorico.text()
        denominador_input = self.denominador_teorico.text()
        self.color_t = self.teorico_color_comboBox.currentText()
        unidad_frec = self.teorico_frec_comboBox.currentText()
        unidad_modulo = self.teorico_modulo_comboBox.currentText()
        unidad_fase = self.teorico_fase_comboBox.currentText()
        if unidad_fase == "grados":
            unidad_fase = "°"
        cs.add_curve(1, [numerador_input, denominador_input], self.nombre_input, self.color_t, unidad_frec, unidad_modulo, unidad_fase)
        self.close()

    def display_ecuacion(self):
        self.line_ecuacion.show()
        numerador = self.numerador_teorico.text()
        denominador = self.denominador_teorico.text()
        num_coef = numerador.split(',')
        den_coef = denominador.split(',')

        num_len = len(num_coef)
        num_str = ""
        for i in range(0, num_len):
            if (num_len - i) > 2:
                num_str += str(num_coef[i]) + ".s^" + str(num_len - 1 - i) + "+"
            elif (num_len - i) == 2:
                num_str += str(num_coef[i]) + ".s +"
            else:
                num_str += str(num_coef[i])

        den_len = len(den_coef)
        den_str = ""
        for i in range(0, den_len):
            if (den_len - i) > 2:
                den_str += str(den_coef[i]) + ".s^" + str(den_len - 1 - i) + "+"
            elif (den_len - i) == 2:
                den_str += str(den_coef[i]) + ".s +"
            else:
                den_str += str(den_coef[i])
        self.label_numerador.setText(num_str)
        self.label_denominador.setText(den_str)

class Input_Simulacion_Window(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi("input_simulacion.ui", self)
        self.setWindowTitle("Input Simulación")

        self.show()
        self.upload_simulacion_pushButton.clicked.connect(self.get_simulation_file)
        self.ok_simulacion_pushButton_2.clicked.connect(self.display_ok)

    def get_simulation_file(self):
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]


    def display_ok(self):
        self.nombre_input = self.nombre_graph_simulacion.text()
        self.color_t = self.simulacion_color_comboBox.currentText()
        unidad_frec = self.simulacion_frec_comboBox.currentText()
        unidad_modulo = self.simulacion_modulo_comboBox.currentText()
        unidad_fase = self.simulacion_fase_comboBox.currentText()
        if unidad_fase == "grados":
            unidad_fase = "°"
        cs.add_curve(2, self.path, self.nombre_input, self.color_t,unidad_frec, unidad_modulo, unidad_fase)
        self.close()

class Input_Medicion_Window(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi("input_medicion.ui", self)
        self.setWindowTitle("Input Medición")

        self.show()
        self.upload_medicion_pushButton.clicked.connect(self.get_medicion_file)
        self.ok_medicion_pushButton_2.clicked.connect(self.display_ok)

    def get_medicion_file(self):
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]

    def display_ok(self):
        self.nombre_input = self.nombre_graph_medicion.text()
        self.color_t = self.medicion_color_comboBox.currentText()
        unidad_frec = self.medicion_frec_comboBox.currentText()
        unidad_modulo = self.medicion_modulo_comboBox.currentText()
        unidad_fase = self.medicion_fase_comboBox.currentText()
        if unidad_fase == "grados":
            unidad_fase = "°"
        cs.add_curve(3, self.path, self.nombre_input, self.color_t, unidad_frec, unidad_modulo, unidad_fase)
        self.close()

class Input_Montecarlo_Window(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi("input_montecarlo.ui", self)
        self.setWindowTitle("Input Montecarlo")

        self.show()
        self.upload_montecarlo_pushButton.clicked.connect(self.get_montecarlo_file)
        self.ok_montecarlo_pushButton_2.clicked.connect(self.display_ok)

    def get_montecarlo_file(self):
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]

    def display_ok(self):
        self.nombre_input = self.nombre_graph_montecarlo.text()
        self.color_t = self.montecarlo_color_comboBox.currentText()
        unidad_frec = self.montecarlo_frec_comboBox.currentText()
        unidad_modulo = self.montecarlo_modulo_comboBox.currentText()
        unidad_fase = self.montecarlo_fase_comboBox.currentText()
        if unidad_fase == "grados":
            unidad_fase = "°"
        cs.add_curve(4, self.path, self.nombre_input, self.color_t, unidad_frec, unidad_modulo, unidad_fase)
        self.close()

class Input_Resp_Temp_Window(QWidget):

    def __init__(self, mainWind):
        QWidget.__init__(self)
        loadUi("input_resp_temp.ui", self)
        self.setWindowTitle("Input Respuesta Temporal")

        self.show()

        self.mainWind = mainWind

        self.resp_temp_teo_label.hide()
        self.resp_temp_teo_comboBox.hide()
        self.curva_teo_comboBox.hide()
        self.teo_aplicar.hide()

        self.resp_temp_simu_label.hide()
        self.resp_temp_simu_upload.hide()
        self.simu_graficar.hide()

        self.t_inicial_resp_temp_label.hide()
        self.t_inicial_resp_temp_line.hide()
        self.t_final_resp_temp_label.hide()
        self.t_final_resp_temp_line.hide()
        self.amp_resp_temp_label.hide()
        self.amp_resp_temp_line.hide()
        self.dc_resp_temp_label.hide()
        self.dc_resp_temp_line.hide()
        self.exp_resp_temp_label.hide()
        self.exp_resp_temp_line.hide()
        self.frec_resp_temp_label.hide()
        self.frec_resp_temp_line.hide()
        self.resp_temp_graficar.hide()

        self.teo_simu_aplicar.clicked.connect(self.display_teo_simu)

    def display_teo_simu(self):
        self.teo_simu = self.resp_temp_teo_simu_comboBox.currentIndex()

        if (self.teo_simu == 0):
            self.resp_temp_teo_simu_label.hide()
            self.resp_temp_teo_simu_comboBox.hide()
            self.teo_simu_aplicar.hide()

            self.resp_temp_teo_label.show()
            self.resp_temp_teo_comboBox.show()
            self.teo_aplicar.show()
            for i in range(len(cs.curves)):
                if cs.curves[i].type == 1:
                    self.curva_teo_comboBox.addItem(cs.curves[i].name)
            self.curva_teo_comboBox.show()
            self.teo_aplicar.clicked.connect(self.display_ok_teo)
        else:
            self.resp_temp_teo_simu_label.hide()
            self.resp_temp_teo_simu_comboBox.hide()
            self.teo_simu_aplicar.hide()

            self.resp_temp_simu_label.show()
            self.resp_temp_simu_upload.show()
            self.simu_graficar.show()
            self.resp_temp_simu_upload.clicked.connect(self.get_simulation_file)
            self.simu_graficar.clicked.connect(self.display_ok_simu)

    def display_ok_teo(self):
        self.resp_temp_graficar.show()
        self.curva_teo_select = self.curva_teo_comboBox.currentText()
        self.teo_curve=0
        for i in range(len(cs.curves)):
            if self.curva_teo_select == cs.curves[i].name:
                self.teo_curve = cs.curves[i]

        self.senal = self.resp_temp_teo_comboBox.currentIndex()

        if (self.senal == 0):  # senoidal
            self.t_inicial_resp_temp_label.show()
            self.t_inicial_resp_temp_line.show()
            self.t_final_resp_temp_label.show()
            self.t_final_resp_temp_line.show()
            self.amp_resp_temp_label.show()
            self.amp_resp_temp_line.show()
            self.frec_resp_temp_label.show()
            self.frec_resp_temp_line.show()

        elif (self.senal == 1):  # escalon
            self.t_inicial_resp_temp_label.show()
            self.t_inicial_resp_temp_line.show()
            self.t_final_resp_temp_label.show()
            self.t_final_resp_temp_line.show()
            self.amp_resp_temp_label.show()
            self.amp_resp_temp_line.show()

        elif (self.senal == 2):  # tren de pulsos
            self.t_inicial_resp_temp_label.show()
            self.t_inicial_resp_temp_line.show()
            self.t_final_resp_temp_label.show()
            self.t_final_resp_temp_line.show()
            self.amp_resp_temp_label.show()
            self.amp_resp_temp_line.show()
            self.dc_resp_temp_label.show()
            self.dc_resp_temp_line.show()
            self.frec_resp_temp_label.show()
            self.frec_resp_temp_line.show()

        elif (self.senal == 3):  # impulso
            self.t_inicial_resp_temp_label.show()
            self.t_inicial_resp_temp_line.show()
            self.t_final_resp_temp_label.show()
            self.t_final_resp_temp_line.show()
            self.amp_resp_temp_label.show()
            self.amp_resp_temp_line.show()

        elif (self.senal == 4):  # rampa
            self.t_inicial_resp_temp_label.show()
            self.t_inicial_resp_temp_line.show()
            self.t_final_resp_temp_label.show()
            self.t_final_resp_temp_line.show()
            self.amp_resp_temp_label.show()
            self.amp_resp_temp_line.show()
            self.dc_resp_temp_label.setText("pendiente")

        elif (self.senal == 5):  # exponencial
            self.t_inicial_resp_temp_label.show()
            self.t_inicial_resp_temp_line.show()
            self.t_final_resp_temp_label.show()
            self.t_final_resp_temp_line.show()
            self.amp_resp_temp_label.show()
            self.amp_resp_temp_line.show()
            self.exp_resp_temp_label.show()
            self.exp_resp_temp_line.show()

        self.resp_temp_graficar.clicked.connect(self.display_fun)

    def display_fun(self):
        self.nombre_input = self.resp_temp_nombre_lineEdit.text()
        self.color_t = self.resp_temp_color_comboBox.currentText()
        self.unidad_tiempo = self.resp_temp_tiempo_comboBox.currentText()
        self.unidad_salida = self.resp_temp_sal_comboBox.currentText()
        self.params = []
        if (self.senal == 0):  # senoidal
            self.ti = self.t_inicial_resp_temp_line.text()
            self.tf = self.t_final_resp_temp_line.text()
            self.amp = self.amp_resp_temp_line.text()
            self.frec = self.frec_resp_temp_line.text()
            self.params=[float(self.amp), float(self.frec)]

        elif (self.senal == 1):  # escalon
            self.ti = self.t_inicial_resp_temp_line.text()
            self.tf = self.t_final_resp_temp_line.text()
            self.amp = self.amp_resp_temp_line.text()
            self.params=[float(self.amp)]

        elif (self.senal == 2):  # tren de pulsos
            self.ti = self.t_inicial_resp_temp_line.text()
            self.tf = self.t_final_resp_temp_line.text()
            self.amp = self.amp_resp_temp_line.text()
            self.dc = self.dc_resp_temp_line.text()
            self.frec = self.frec_resp_temp_line.text()
            self.params=[float(self.amp), float(self.frec), float(self.dc)]

        elif (self.senal == 3):  # impulso
            self.ti = self.t_inicial_resp_temp_line.text()
            self.tf = self.t_final_resp_temp_line.text()
            self.amp = self.amp_resp_temp_line.text()
            self.params=[float(self.amp)]

        elif (self.senal == 4):  # rampa
            self.ti = self.t_inicial_resp_temp_line.text()
            self.tf = self.t_final_resp_temp_line.text()
            self.amp = self.amp_resp_temp_line.text()
            self.dc_resp_temp_label.setText("pendiente")
            self.pendiente = self.dc_resp_temp_line.text()
            self.params=[float(self.amp), float(self.pendiente)]

        elif (self.senal == 5):  # exponencial
            self.ti = self.t_inicial_resp_temp_line.text()
            self.tf = self.t_final_resp_temp_line.text()
            self.amp = self.amp_resp_temp_line.text()
            self.exp = self.exp_resp_temp_line.text()
            self.params=[float(self.amp), float(self.exp)]

        ts.add_curve(self.senal+1, [self.teo_curve, np.linspace(float(self.ti), float(self.tf)), self.params], self.nombre_input, self.color_t, self.unidad_tiempo, self.unidad_salida)
        self.close()
        self.mainWind.addCurveTemp()
        window.show_graph()

    def get_simulation_file(self):
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]

    def display_ok_simu(self):
        self.nombre_input = self.resp_temp_nombre_lineEdit.text()
        self.color_t = self.resp_temp_color_comboBox.currentText()
        self.unidad_tiempo = self.resp_temp_tiempo_comboBox.currentText()
        self.unidad_salida = self.resp_temp_sal_comboBox.currentText()

        ts.add_curve(0, self.path, self.nombre_input, self.color_t, self.unidad_tiempo, self.unidad_salida)
        self.close()
        self.mainWind.addCurveTemp()
        window.show_graph()

#Modificar
class Input_Teorico_Window_Modificar(QWidget):

    def __init__(self, mainWin):
        QWidget.__init__(self)
        loadUi("input_teorico_modificar.ui", self)
        self.setWindowTitle("Input Teórico Modificar")

        self.mainWind = mainWin
        self.show()
        self.line_ecuacion_m.hide()
        self.ok_teorico_pushButton_m.clicked.connect(self.display_ok)
        self.ecuacion_teorico_pushButton_m.clicked.connect(self.display_ecuacion)
        self.cancel_teorico_pushButton_m.clicked.connect(self.close)


    def display_ok(self):
        self.nombre_input = self.nombre_graph_teorico_m.text()
        numerador_input = self.numerador_teorico_m.text()
        denominador_input = self.denominador_teorico_m.text()
        self.color_t = self.teorico_color_comboBox_m.currentText()
        unidad_frec = self.teorico_frec_comboBox_m.currentText()
        unidad_modulo = self.teorico_modulo_comboBox_m.currentText()
        unidad_fase = self.teorico_fase_comboBox_m.currentText()
        if unidad_fase == "grados":
            unidad_fase = "°"
        cs.update(self.mainWind.index, [numerador_input, denominador_input], self.nombre_input, self.color_t, unidad_frec, unidad_modulo, unidad_fase)
        self.close()
        window.show_graph()
        self.mainWind.update_name(cs.curves[self.mainWind.index].name)

    def display_ecuacion(self):
        self.line_ecuacion_m.show()
        numerador = self.numerador_teorico_m.text()
        denominador = self.denominador_teorico_m.text()
        num_coef = numerador.split(',')
        den_coef = denominador.split(',')

        num_len = len(num_coef)
        num_str = ""
        for i in range(0, num_len):
            if (num_len - i) > 2:
                num_str += str(num_coef[i]) + ".s^" + str(num_len - 1 - i) + "+"
            elif (num_len - i) == 2:
                num_str += str(num_coef[i]) + ".s +"
            else:
                num_str += str(num_coef[i])

        den_len = len(den_coef)
        den_str = ""
        for i in range(0, den_len):
            if (den_len - i) > 2:
                den_str += str(den_coef[i]) + ".s^" + str(den_len - 1 - i) + "+"
            elif (den_len - i) == 2:
                den_str += str(den_coef[i]) + ".s +"
            else:
                den_str += str(den_coef[i])
        self.label_numerador_m.setText(num_str)
        self.label_denominador_m.setText(den_str)

class Input_Simulacion_Window_Modificar(QWidget):

    def __init__(self, mainWin):
        QWidget.__init__(self)
        loadUi("input_simulacion_modificar.ui", self)
        self.setWindowTitle("Input Simulación Modificar")

        self.mainWind = mainWin
        self.show()
        self.upload_simulacion_pushButton_m.clicked.connect(self.get_simulation_file)
        self.ok_simulacion_pushButton_2_m.clicked.connect(self.display_ok)

    def get_simulation_file(self):
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]


    def display_ok(self):
        self.nombre_input = self.nombre_graph_simulacion_m.text()
        self.color_t = self.simulacion_color_comboBox_m.currentText()
        unidad_frec = self.simulacion_frec_comboBox_m.currentText()
        unidad_modulo = self.simulacion_modulo_comboBox_m.currentText()
        unidad_fase = self.simulacion_fase_comboBox_m.currentText()
        if unidad_fase == "grados":
            unidad_fase = "°"
        cs.update(self.mainWind.index, self.path, self.nombre_input, self.color_t,unidad_frec, unidad_modulo, unidad_fase)
        self.close()
        window.show_graph()
        self.mainWind.update_name(cs.curves[self.mainWind.index].name)

class Input_Medicion_Window_Modificar(QWidget):

    def __init__(self, mainWin):
        QWidget.__init__(self)
        loadUi("input_medicion_modificar.ui", self)
        self.setWindowTitle("Input Medición Modificar")

        self.mainWind = mainWin
        self.show()
        self.upload_medicion_pushButton_m.clicked.connect(self.get_medicion_file)
        self.ok_medicion_pushButton_2_m.clicked.connect(self.display_ok)

    def get_medicion_file(self):
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]

    def display_ok(self):
        self.nombre_input = self.nombre_graph_medicion_m.text()
        self.color_t = self.medicion_color_comboBox_m.currentText()
        unidad_frec = self.medicion_frec_comboBox_m.currentText()
        unidad_modulo = self.medicion_modulo_comboBox_m.currentText()
        unidad_fase = self.medicion_fase_comboBox_m.currentText()
        if unidad_fase == "grados":
            unidad_fase = "°"
        cs.update(self.mainWind.index, self.path, self.nombre_input, self.color_t, unidad_frec, unidad_modulo, unidad_fase)
        self.close()
        window.show_graph()
        self.mainWind.update_name(cs.curves[self.mainWind.index].name)

class Input_Montecarlo_Window_Modificar(QWidget):

    def __init__(self, mainWin):
        QWidget.__init__(self)
        loadUi("input_montecarlo_modificar.ui", self)
        self.setWindowTitle("Input Montecarlo Modificar")

        self.mainWind = mainWin
        self.show()
        self.upload_montecarlo_pushButton_m.clicked.connect(self.get_montecarlo_file)
        self.ok_montecarlo_pushButton_2_m.clicked.connect(self.display_ok)

    def get_montecarlo_file(self):
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]

    def display_ok(self):
        self.nombre_input = self.nombre_graph_montecarlo_m.text()
        self.color_t = self.montecarlo_color_comboBox_m.currentText()
        unidad_frec = self.montecarlo_frec_comboBox_m.currentText()
        unidad_modulo = self.montecarlo_modulo_comboBox_m.currentText()
        unidad_fase = self.montecarlo_fase_comboBox_m.currentText()
        if unidad_fase == "grados":
            unidad_fase = "°"
        cs.update(self.mainWind.index, self.path, self.nombre_input, self.color_t, unidad_frec, unidad_modulo, unidad_fase)
        self.close()
        window.show_graph()
        self.mainWind.update_name(cs.curves[self.mainWind.index].name)

class Input_Resp_Temp_Window_Modificar_Teo(QWidget):

    def __init__(self, mainWin):
        QWidget.__init__(self)
        loadUi("input_resp_temp_modificar.ui", self)
        self.setWindowTitle("Input Respuesta Temporal")

        self.show()

        self.mainWin = mainWin

        self.senal = self.mainWin.type_list

        if (self.senal == 1):  # senoidal
            self.dc_resp_temp_label_m.hide()
            self.dc_resp_temp_line_m.hide()
            self.exp_resp_temp_label_m.hide()
            self.exp_resp_temp_line_m.hide()

        elif (self.senal == 2):  # escalon
            self.frec_resp_temp_label_m.hide()
            self.frec_resp_temp_line_m.hide()
            self.dc_resp_temp_label_m.hide()
            self.dc_resp_temp_line_m.hide()
            self.exp_resp_temp_label_m.hide()
            self.exp_resp_temp_line_m.hide()

        elif (self.senal == 3):  # tren de pulsos
            self.exp_resp_temp_label_m.hide()
            self.exp_resp_temp_line_m.hide()

        elif (self.senal == 4):  # impulso
            self.frec_resp_temp_label_m.hide()
            self.frec_resp_temp_line_m.hide()
            self.dc_resp_temp_label_m.hide()
            self.dc_resp_temp_line_m.hide()
            self.exp_resp_temp_label_m.hide()
            self.exp_resp_temp_line_m.hide()

        elif (self.senal == 5):  # rampa
            self.frec_resp_temp_label_m.hide()
            self.frec_resp_temp_line_m.hide()
            self.dc_resp_temp_label_m.hide()
            self.dc_resp_temp_line_m.hide()
            self.exp_resp_temp_label_m.hide()
            self.exp_resp_temp_line_m.hide()
            self.dc_resp_temp_label_m.setText("pendiente")

        elif (self.senal == 6):  # exponencial
            self.dc_resp_temp_label_m.hide()
            self.dc_resp_temp_line_m.hide()
            self.frec_resp_temp_label_m.hide()
            self.frec_resp_temp_line_m.hide()

        self.resp_temp_graficar_m.clicked.connect(self.display_fun)

    def display_fun(self):
        self.nombre_input = self.resp_temp_nombre_lineEdit_m.text()
        self.color_t = self.resp_temp_color_comboBox_m.currentText()
        self.unidad_tiempo = self.resp_temp_tiempo_comboBox_m.currentText()
        self.unidad_salida = self.resp_temp_sal_comboBox_m.currentText()
        self.params = []
        if (self.senal == 1):  # senoidal
            self.ti = self.t_inicial_resp_temp_line_m.text()
            self.tf = self.t_final_resp_temp_line_m.text()
            self.amp = self.amp_resp_temp_line_m.text()
            self.frec = self.frec_resp_temp_line_m.text()
            self.params=[float(self.amp), float(self.frec)]

        elif (self.senal == 2):  # escalon
            self.ti = self.t_inicial_resp_temp_line_m.text()
            self.tf = self.t_final_resp_temp_line_m.text()
            self.amp = self.amp_resp_temp_line_m.text()
            self.params=[float(self.amp)]

        elif (self.senal == 3):  # tren de pulsos
            self.ti = self.t_inicial_resp_temp_line_m.text()
            self.tf = self.t_final_resp_temp_line_m.text()
            self.amp = self.amp_resp_temp_line_m.text()
            self.dc = self.dc_resp_temp_line_m.text()
            self.frec = self.frec_resp_temp_line_m.text()
            self.params=[float(self.amp), float(self.frec), float(self.dc)]

        elif (self.senal == 4):  # impulso
            self.ti = self.t_inicial_resp_temp_line_m.text()
            self.tf = self.t_final_resp_temp_line_m.text()
            self.amp = self.amp_resp_temp_line_m.text()
            self.params=[float(self.amp)]

        elif (self.senal == 5):  # rampa
            self.ti = self.t_inicial_resp_temp_line_m.text()
            self.tf = self.t_final_resp_temp_line_m.text()
            self.amp = self.amp_resp_temp_line_m.text()
            self.dc_resp_temp_label_m.setText("pendiente")
            self.pendiente = self.dc_resp_temp_line_m.text()
            self.params=[float(self.amp), float(self.pendiente)]

        elif (self.senal == 6):  # exponencial
            self.ti = self.t_inicial_resp_temp_line_m.text()
            self.tf = self.t_final_resp_temp_line_m.text()
            self.amp = self.amp_resp_temp_line_m.text()
            self.exp = self.exp_resp_temp_line_m.text()
            self.params=[float(self.amp), float(self.exp)]

        self.teo_curve = cs.curves[self.mainWin.index]
        ts.update(self.mainWin.index, [self.teo_curve, np.linspace(float(self.ti), float(self.tf)), self.params], self.nombre_input, self.color_t, self.unidad_tiempo, self.unidad_salida)
        self.close()
        if len(self.nombre_input) == 0:
            self.mainWin.update_name(cs.curves[self.mainWin.index].name)
        else:
            self.mainWin.update_name(self.nombre_input)
        window.show_graph()

class Input_Resp_Temp_Window_Modificar_Simu(QWidget):

    def __init__(self, mainWin):
        QWidget.__init__(self)
        loadUi("input_simu_resp_temp.ui", self)
        self.setWindowTitle("Input Respuesta Temporal Modificar Simulacion")

        self.show()
        self.mainWin = mainWin

        self.simu_upload.clicked.connect(self.get_simulation_file)
        self.simu_graficar_m.clicked.connect(self.display_ok_simu)

    def get_simulation_file(self):
        filename = QFileDialog.getOpenFileNames()
        self.path = filename[0][0]

    def display_ok_simu(self):
        self.nombre_input = self.simu_nombre.text()
        self.color_t = self.simu_color.currentText()
        self.unidad_tiempo = self.resp_temp_tiempo_comboBox_m.currentText()
        self.unidad_salida = self.resp_temp_sal_comboBox_m.currentText()

        ts.update(self.mainWin.index, self.path, self.nombre_input, self.color_t, self.unidad_tiempo, self.unidad_salida)
        self.close()
        if self.nombre_input == "":
            self.mainWin.update_name(cs.curves[self.mainWin.index].name)
        else:
            self.mainWin.update_name(self.nombre_input)
        window.show_graph()
        window.show_graph()

#MAIN_WINDOW
class MatplotlibWidget(QtWidgets.QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("menu.ui", self)
        self.setWindowTitle("Plot Tool")
        self.MplWidget.make_ToolBar(self.ToolBar1)
        self.MplWidget2.make_ToolBar(self.ToolBar2)
        self.MplWidget3.make_ToolBar(self.ToolBar3)

        self.Curve_0.hide()
        self.Curve_1.hide()
        self.Curves_in_the_List = []
        self.Temp_in_the_List = []

        self.teoricoButton.clicked.connect(self.goto_graphInfoTeorico)
        self.simulacionButton.clicked.connect(self.goto_graphInfoSimulacion)
        self.medicionButton.clicked.connect(self.goto_graphInfoMedicion)
        self.montecarloButton.clicked.connect(self.goto_graphInfoMontecarlo)
        self.resptempButton.clicked.connect(self.goto_graphInfoRespTemp)

        self.borrarpushButton.clicked.connect(self.goto_Borrar_Graficos)

        self.aplicar_button_ejes1.clicked.connect(self.goto_graphModulo_Axis)
        self.aplicar_button_ejes2.clicked.connect(self.goto_graphFase_Axis)
        self.aplicar_button_ejes3.clicked.connect(self.goto_graphTemp_Axis)
        self.aplicar_titulo_1.clicked.connect(self.goto_graphTitulo_1)
        self.aplicar_titulo_2.clicked.connect(self.goto_graphTitulo_2)
        self.aplicar_titulo_3.clicked.connect(self.goto_graphTitulo_3)
        self.aplicar_fig1.clicked.connect(self.goto_unit_fig1)
        self.aplicar_fig2.clicked.connect(self.goto_unit_fig2)
        self.aplicar_fig3.clicked.connect(self.goto_unit_fig3)

    def goto_unit_fig1(self):
        self.fig1_x_comboBox = self.fig1_x_unit.currentText()
        self.fig1_y_comboBox = self.fig1_y_unit.currentText()
        cs.change_w_unit(self.fig1_x_comboBox)
        cs.change_mod_unit(self.fig1_y_comboBox)
        self.show_graph()

    def goto_unit_fig2(self):
        self.fig2_x_comboBox = self.fig2_x_unit.currentText()
        self.fig2_y_comboBox = self.fig2_y_unit.currentText()
        cs.change_w_unit(self.fig2_x_comboBox)
        cs.change_ph_unit(self.fig2_y_comboBox)
        self.show_graph()

    def goto_unit_fig3(self):
        self.fig3_x_comboBox = self.fig3_x_unit.currentText()
        self.fig3_y_comboBox = self.fig3_y_unit.currentText()
        ts.change_t_unit(self.fig3_x_comboBox)
        ts.change_y_unit(self.fig3_y_comboBox)
        self.show_graph()

    def goto_graphInfoTeorico(self):
        self.Input_Teorico = Input_Teorico_Window()
        self.Input_Teorico.ok_teorico_pushButton.clicked.connect(self.addCurveTeorico)
        self.Input_Teorico.cancel_teorico_pushButton.clicked.connect(self.close)

    def goto_graphInfoSimulacion(self):
        self.Input_Simulacion = Input_Simulacion_Window()
        self.Input_Simulacion.ok_simulacion_pushButton_2.clicked.connect(self.addCurveSimulacion)

    def goto_graphInfoMedicion(self):
        self.Input_Medicion = Input_Medicion_Window()
        self.Input_Medicion.ok_medicion_pushButton_2.clicked.connect(self.addCurveMedicion)

    def goto_graphInfoMontecarlo(self):
        self.Input_Montecarlo = Input_Montecarlo_Window()
        self.Input_Montecarlo.ok_montecarlo_pushButton_2.clicked.connect(self.addCurveMontecarlo)

    def goto_graphInfoRespTemp(self):
        self.Input_Resp_Temp = Input_Resp_Temp_Window(self)

    def addCurveTeorico(self):
        if len(cs.curves) != 0:
            aux_curve = ListWidget(self)
            self.Curves_in_the_List.append(aux_curve)
            self.CurveList.layout().addWidget(aux_curve)
        self.show_graph()

    def addCurveTemp(self):
        if len(ts.curves) != 0:
            aux_curve = ListWidget2(self)
            self.Temp_in_the_List.append(aux_curve)
            self.CurveList_2.layout().addWidget(aux_curve)
        self.show_graph()

    def addCurveSimulacion(self):
        if len(cs.curves) != 0:
            aux_curve = ListWidget(self)
            self.Curves_in_the_List.append(aux_curve)
            self.CurveList.layout().addWidget(aux_curve)
        self.show_graph()

    def addCurveMedicion(self):
        if len(cs.curves) != 0:
            aux_curve = ListWidget(self)
            self.Curves_in_the_List.append(aux_curve)
            self.CurveList.layout().addWidget(aux_curve)
        self.show_graph()

    def addCurveMontecarlo(self):
        if len(cs.curves) != 0:
            aux_curve = ListWidget(self)
            self.Curves_in_the_List.append(aux_curve)
            self.CurveList.layout().addWidget(aux_curve)
        self.show_graph()


    def goto_graphModulo_Axis(self):
        if len(self.ejex_lineEdit.text()) == 0:
            ax_x = "Eje X"
        else:
            ax_x = self.ejex_lineEdit.text()
        if len(self.ejey_lineEdit.text()) == 0:
            ax_y = "Eje Y"
        else:
            ax_y = self.ejey_lineEdit.text()

        cs.change_x_mod_label(ax_x)
        cs.change_y_mod_label(ax_y)
        self.ejex_lineEdit.setText("")
        self.ejey_lineEdit.setText("")
        self.show_graph()


    def goto_graphFase_Axis(self):
        if len(self.ejex2_lineEdit.text()) == 0:
            ax_x = "Eje X"
        else:
            ax_x = self.ejex2_lineEdit.text()
        if len(self.ejey2_lineEdit.text()) == 0:
            ax_y = "Eje Y"
        else:
            ax_y = self.ejey2_lineEdit.text()

        cs.change_x_ph_label(ax_x)
        cs.change_y_ph_label(ax_y)
        self.ejex2_lineEdit.setText("")
        self.ejey2_lineEdit.setText("")
        self.show_graph()

    def goto_graphTemp_Axis(self):
        if len(self.ejex3_lineEdit.text()) == 0:
            ax_t = "Eje T"
        else:
            ax_t = self.ejex3_lineEdit.text()
        if len(self.ejey3_lineEdit.text()) == 0:
            ax_y = "Eje Y"
        else:
            ax_y = self.ejey3_lineEdit.text()

        ts.change_t_label(ax_t)
        ts.change_y_label(ax_y)
        self.ejex3_lineEdit.setText("")
        self.ejey3_lineEdit.setText("")
        self.show_graph()

    def goto_graphTitulo_1(self):
        if len(self.Titulo_1.text()) == 0:
            titulo = "Módulo"
        else:
            titulo = self.Titulo_1.text()

        cs.change_mod_title(titulo)
        self.Titulo_1.setText("")
        self.show_graph()

    def goto_graphTitulo_2(self):
        if len(self.Titulo_2.text()) == 0:
            titulo = "Fase"
        else:
            titulo = self.Titulo_2.text()

        cs.change_ph_title(titulo)
        self.Titulo_2.setText("")
        self.show_graph()

    def goto_graphTitulo_3(self):
        if len(self.Titulo_3.text()) == 0:
            titulo = "Respuesta Temporal"
        else:
            titulo = self.Titulo_3.text()

        ts.change_title(titulo)
        self.Titulo_3.setText("")
        self.show_graph()

    def update_Curve_in_the_List(self, index_deleted_widget):
        #self.Curves_in_the_List[index_deleted_widget].goto_borrar()
        self.Curves_in_the_List.pop(index_deleted_widget)
        for i in range(index_deleted_widget, len(self.Curves_in_the_List)):
            self.Curves_in_the_List[i].update_index(i)

    def update_Temp_in_the_List(self, index_deleted_widget):
        #self.Curves_in_the_List[index_deleted_widget].goto_borrar()
        self.Temp_in_the_List.pop(index_deleted_widget)
        for i in range(index_deleted_widget, len(self.Temp_in_the_List)):
            self.Temp_in_the_List[i].update_index(i)


    def show_graph(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget2.canvas.axes.clear()
        self.MplWidget3.canvas.axes.clear()
        print(len(cs.curves))
        if len(cs.curves) != 0:
            cs.plot_mod(self.MplWidget.canvas.axes)
            cs.plot_ph(self.MplWidget2.canvas.axes)
            self.MplWidget.canvas.draw()
            self.MplWidget2.canvas.draw()
        else:
            self.hide_frec_graph()
        if len(ts.curves) != 0:
            ts.plot_time(self.MplWidget3.canvas.axes)
            self.MplWidget3.canvas.draw()
        else:
            self.hide_resp_graph()

    def hide_frec_graph(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.draw()
        self.MplWidget2.canvas.axes.clear()
        self.MplWidget2.canvas.draw()

    def hide_resp_graph(self):
        self.MplWidget3.canvas.axes.clear()
        self.MplWidget3.canvas.draw()

    def hide_graph(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.draw()
        self.MplWidget2.canvas.axes.clear()
        self.MplWidget2.canvas.draw()
        self.MplWidget3.canvas.axes.clear()
        self.MplWidget3.canvas.draw()

    def goto_Borrar_Graficos(self):
        while len(self.Curves_in_the_List) != 0:
            self.Curves_in_the_List[0].goto_borrar()
        while len(self.Temp_in_the_List) != 0:
            self.Temp_in_the_List[0].goto_borrar()
        #for i in range(len(self.Curves_in_the_List))[::-1]:
        #    self.Curves_in_the_List[i].goto_borrar()
        #    self.Curves_in_the_List.pop(i)
        #for i in range(len(cs.curves)):
        #    cs.del_curve(cs.curves[0])
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.draw()
        self.MplWidget2.canvas.axes.clear()
        self.MplWidget2.canvas.draw()
        self.MplWidget3.canvas.axes.clear()
        self.MplWidget3.canvas.draw()


#List Widgets
class ListWidget(QWidget):

    def __init__(self, mainWindow):
        QMainWindow.__init__(self)
        loadUi("ListWidget.ui", self)

        self.nombre_list.setText(cs.curves[-1].name)
        self.type_list = cs.curves[-1].type
        self.mainWindow = mainWindow
        self.visibilidad_list.clicked.connect(self.goto_visibilidad)
        self.modificar_list.clicked.connect(self.goto_modificar)
        self.borrar_list.clicked.connect(self.goto_borrar)
        self.index = cs.curves.index(cs.curves[-1])

    def goto_visibilidad(self):
        cs.curves[self.index].change_visibility()
        window.show_graph()

    def goto_modificar(self):
        if self.type_list == 1:
            self.Input_Teorico_Modificar = Input_Teorico_Window_Modificar(self)
        elif self.type_list == 2:
            self.Input_Simulacion_Modificar = Input_Simulacion_Window_Modificar(self)
        elif self.type_list == 3:
            self.Input_Medicion_Modificar = Input_Medicion_Window_Modificar(self)
        elif self.type_list == 4:
            self.Input_Montecarlo_Modificar = Input_Montecarlo_Window_Modificar(self)

    def update_name(self, new_name):
        self.nombre_list.setText(new_name)

    def update_index(self, new_index):
        self.index = new_index

    def goto_borrar(self):
        cs.del_curve(cs.curves[self.index])
        self.hide()
        window.show_graph()
        self.mainWindow.update_Curve_in_the_List(self.index)

class ListWidget2(QWidget):

        def __init__(self, mainWindow):
            QMainWindow.__init__(self)
            loadUi("ListWidget.ui", self)

            self.nombre_list.setText(ts.curves[-1].name)
            self.type_list = ts.curves[-1].type
            self.mainWindow = mainWindow
            self.visibilidad_list.clicked.connect(self.goto_visibilidad)
            self.modificar_list.clicked.connect(self.goto_modificar)
            self.borrar_list.clicked.connect(self.goto_borrar)
            self.index = ts.curves.index(ts.curves[-1])

        def goto_visibilidad(self):
            ts.curves[self.index].change_visibility()
            window.show_graph()

        def goto_modificar(self):
            if self.type_list == 0:
                self.Input_Resp_Temp_Modificar = Input_Resp_Temp_Window_Modificar_Simu(self)
            else:
                self.Input_Resp_Temp_Modificar = Input_Resp_Temp_Window_Modificar_Teo(self)

        def update_name(self, new_name):
            self.nombre_list.setText(new_name)

        def update_index(self, new_index):
            self.index = new_index

        def goto_borrar(self):
            ts.del_curve(ts.curves[self.index])
            self.hide()
            window.show_graph()
            self.mainWindow.update_Temp_in_the_List(self.index)


cs = Frecspace()
ts = Timespace()
app = QApplication([])
window = MatplotlibWidget()
window.show()
try:
    sys.exit(app.exec_())
except:
    print("saliendo")