import numpy as np
import scipy.signal as ss
import os
import matplotlib.lines as mlines
from curvespace import Curvespace, Curve

########################################################################################################################
# Clase Frecspace: Contiene la lista de curvas de frecuencias y métodos para modificarla
# ----------------------------------------------------------------------------------------------------------------------
class Frecspace(Curvespace):
    def __init__(self):
        super().__init__()

        self.w_unit = "Hz"      # Unidad de la frecuencia del gráfico
        self.mod_unit = "dB"    # Unidad de módulo del gráfico
        self.ph_unit = "°"      # Unidad de fase del gráfico
        self.x_mod_label = "$f$"            # Label del eje x del gráfico del módulo. Es f por defecto
        self.y_mod_label = "$|H(s)|$"       # Label del eje y del gráfico del módulo. Es |H(s)| por defecto
        self.x_ph_label = "$f$"             # Label del eje x del gráfico de la fase. Es f por defecto
        self.y_ph_label = "$\\phi(H(s))$"   # Label del eje y del gráfico de la fase. Es phi(H(s)) por defecto
        self.title = "Respuesta en frecuencia"      # Título del gráfico
        self.mod_title = "Módulo"                   # Título del gráfico de módulo
        self.ph_title = "Fase"                      # Título del gráfico de fase

    # update: Método para actualizar los valores de la curva sin tener que borrarla y crearla de vuelta
    # OJO: En vez de recibir el tipo de curva, recibe el índice
    def update(self, index, data, name="", color="", w_unit="Hz", mod_unit="dB", ph_unit="°"):
        self.change_curve_name(index, name)
        self.change_curve_color(index, color)
        self.curves[index].change_w_unit(w_unit)
        self.curves[index].change_mod_unit(mod_unit)
        self.curves[index].change_ph_unit(ph_unit)
        self.curves[index].change_data(data)

    # addCurve: Método para agregar una curva. Para más detalles mirar clase Curva
    def add_curve(self, c_type, data, name="", color="", w_unit="rad/s", mod_unit="dB", ph_unit="°"):
        if name == "" or not self.check_name(name):
            for i in range(len(self.curves) + 1):
                name = "Curve " + str(len(self.curves) - i)
                if self.check_name(name):
                    print("Se tomará como nombre: " + name)
                    break
        # SWITCH DE COLORES
        switch_colors = ["blue", "orange", "green", "red", "cyan", "magenta", "gold", "violet"]
        if color == "":# and c_type != 4:
            color = switch_colors[len(self.curves) % 8]
            print("Para la curva", name, "se tomará el color: " + color)

        if not self.switch_ctypes.get(c_type)(self, data, name, color, w_unit, mod_unit, ph_unit):
            print("Error creando la curva")

    # plot_mod: grafica el módulo del conjunto de curvas visibles, si alguna da error deja de ser visible
    def plot_mod(self, ax):
        self.fix_units()
        h = []
        for i in range(len(self.curves)):
            if self.curves[i].visibility:
                if self.curves[i].plot_curve_mod(ax):  # Grafico módulo
                    h.append(mlines.Line2D([], [], color=self.curves[i].color, label=self.curves[i].name))
                else: self.curves[i].visibility = False
        ax.legend(handles=h)
        ax.set_title(self.mod_title)
        ax.set_xlabel(self.x_mod_label + " $\\left[" + self.curves[0].w_unit + "\\right]$")
        ax.set_ylabel(self.y_mod_label + " $\\left[" + self.curves[0].mod_unit + "\\right]$")
        ax.grid()
        return

    # plot_ph: grafica la fase del conjunto de curvas visibles, si alguna da error deja de ser visible
    def plot_ph(self, ax):
        self.fix_units()
        h = []
        for i in range(len(self.curves)):
            if self.curves[i].visibility:
                if self.curves[i].plot_curve_ph(ax):  # Grafico fase
                    h.append(mlines.Line2D([], [], color=self.curves[i].color, label=self.curves[i].name))
                else: self.curves[i].visibility = False
        ax.legend(handles=h)
        if self.ph_unit == "°":
            ax.set_yticks([-180, -135, -90, -45, 0, 45, 90, 135, 180])
        elif self.ph_unit == "rad":
            ax.set_yticks([-np.pi, -3*np.pi/4, -np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
            ax.set_yticklabels(["$-\\pi$", "$-\\frac{3}{4} \\pi$", "$-\\frac{\\pi}{2}$", "$-\\frac{\\pi}{4}$", 0, "$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$", "$\\frac{3}{4} \\pi$", "$\\pi$"])
        ax.set_title(self.ph_title)
        ax.set_xlabel(self.x_ph_label + " $\\left[" + self.curves[0].w_unit + "\\right]$")
        ax.set_ylabel(self.y_ph_label + " $\\left[" + self.curves[0].ph_unit + "\\right]$")
        ax.grid()
        return

    # change_title: Setter para el título del gráfico
    # Devuelve False en caso de error
    def change_title(self, title):
        r = False
        if isinstance(title, str):
            self.title = title
            r = True
        return r

    # change_mod_title: Setter para el título del gráfico del módulo
    # Devuelve False en caso de error
    def change_mod_title(self, title):
        r = False
        if isinstance(title, str):
            self.mod_title = title
            r = True
        return r

    # change_ph_title: Setter para el título del gráfico de la fase
    # Devuelve False en caso de error
    def change_ph_title(self, title):
        r = False
        if isinstance(title, str):
            self.ph_title = title
            r = True
        return r

    # change_x_mod_label: Cambia el label del eje x del gráfico del módulo
    def change_x_mod_label(self, label):
        if label == "f":
            self.x_mod_label = "$f$"
        elif label == "w":
            self.x_mod_label = "$\\omega$"
        else:
            self.x_mod_label = label

    # change_y_mod_label: Cambia el label del eje y del gráfico del módulo
    def change_y_mod_label(self, label):
        if label == "|H(s)|":
            self.y_mod_label = "$|H(s)|$"
        else:
            self.y_mod_label = label

    # change_x_ph_label: Cambia el label del eje x del gráfico de la fase
    def change_x_ph_label(self, label):
        if label == "f":
            self.x_ph_label = "$f$"
        elif label == "w":
            self.x_ph_label = "$\\omega$"
        else:
            self.x_ph_label = label

    # change_y_mod_label: Cambia el label del eje y del gráfico de la fase
    def change_y_ph_label(self, label):
        if label == "phi(H(s))":
            self.y_ph_label = "$\\phi(H(s))$"
        else:
            self.y_ph_label = label

    # change_w_unit: Cambia la unidad de la frecuencia de Hz a rad/s o viceversa
    # Si no se especifica la unidad a la que se quiere cambiar o es una que no existe, hace un switch
    def change_w_unit(self, unit=""):
        if unit == "rad/seg" or unit == "rad/s":
            unit = "\\frac{rad}{s}"
        if self.w_unit != unit:
            if self.w_unit == "Hz":
                self.w_unit = "\\frac{rad}{s}"
            else:
                self.w_unit = "Hz"
        return

    # change_mod_unit: Cambia la unidad del módulo de dB a ?? o viceversa
    # Si no se especifica la unidad a la que se quiere cambiar o es una que no existe, hace un switch
    def change_mod_unit(self, unit=""):
        if self.mod_unit != unit:
            if self.mod_unit == "dB":
                self.mod_unit = "veces"
            else:
                self.mod_unit = "dB"
        return

    # change_ph_unit: Cambia la unidad de la fase de ° a rad o viceversa
    # Si no se especifica la unidad a la que se quiere cambiar o es una que no existe, hace un switch
    def change_ph_unit(self, unit=""):
        if self.ph_unit != unit:
            if self.ph_unit == "°":
                self.ph_unit = "rad"
            else:
                self.ph_unit = "°"
        return

    # fix_units: Revisa las unidades de cada curva visible para que todas tengan las especificadas y tenga sentido graficarlas
    def fix_units(self):
        for i in range(len(self.curves)):
            if self.curves[i].visibility:
                self.curves[i].change_w_unit(self.w_unit)
                self.curves[i].change_mod_unit(self.mod_unit)
                self.curves[i].change_ph_unit(self.ph_unit)

    def teorica(self, data, name, color, w_unit="Hz", mod_unit="dB", ph_unit="°"):
        # print("teórica")
        r = True
        t = Teo(1, data, name, color, w_unit, mod_unit, ph_unit)
        if t.H is not None:
            self.curves.append(t)
        else:
            print("Los datos ingresados no son válidos")
            r = False
        return r

    def simulada(self, data, name, color, w_unit="Hz", mod_unit="dB", ph_unit="°"):
        # print("simulada")
        r = True
        s = Sim(2, data, name, color, w_unit, mod_unit, ph_unit)
        if s.w != [] and s.mod != [] and s.ph != []:
            self.curves.append(s)
        else:
            print("Los datos ingresados no son válidos")
            r = False
        return r

    def medida(self, data, name, color, w_unit="Hz", mod_unit="dB", ph_unit="°"):
        # print("medida")
        r = True
        m = Med(3, data, name, color, w_unit, mod_unit, ph_unit)
        if m.w != [] and m.mod != [] and m.ph != []:
            self.curves.append(m)
        else:
            print("Los datos ingresados no son válidos")
            r = False
        return r

    def montecarlo(self, data, name, color, w_unit="Hz", mod_unit="dB", ph_unit="°"):
        # print("montecarlo")
        r = True
        mc = MC(4, data, name, color, w_unit, mod_unit, ph_unit)
        if mc.w != [] and mc.mod != [] and mc.ph != []:
            self.curves.append(mc)
        else:
            print("Los datos ingresados no son válidos")
            r = False
        return r

    def c_type_error(self):
        print("Si llegó hasta acá es porque se rompió algo")
        return False

    # SWITCH
    switch_ctypes = {
        1: teorica,
        2: simulada,
        3: medida,
        4: montecarlo,
    }
########################################################################################################################

########################################################################################################################
# Clase FrecCurve: Contiene toda la información para graficar la curva de frecuencia. Necesita:
#    - Tipo de curva: - 1 si es teórica (función transferencia)
#                     - 2 si es simulada (LTSpice)
#                     - 3 si es medida (Digilent)
#                     - 4 si es monte carlo (LTSpice)
#                     - 0 si es otra cosa (error)
#    - Raw Data: Dependerán del tipo de curva, en cada caso se especifica mejor (mirar funciones)
#    - Nombre: Si no se especifica, se le asignará uno según el orden
#    - Color: Se permitirá elegir el color de la curva, si no se especifica se tomará naranja
#    - Visibilidad: True si la curva está visible, False si está oculta
#    - w: Intervalo de frecuencias (Arreglo vacío si hubo error)
#    - mod: Módulo de la transferencia (Arreglo vacío si hubo error)
#    - ph: Fase de la trasferencia (Arreglo vacío si hubo error)
#    - w_unit: Unidad de la frecuencia, por defecto es Hz (En LaTex)
#    - mod_unit: Unidad del módulo, por defecto es dB (En LaTex)
#    - ph_unit: Unidad de la fase, por defecto es ° (En LaTex)
# Para cada tipo se accede una clase particular, mirarlas para más detalles
# ----------------------------------------------------------------------------------------------------------------------
class FrecCurve(Curve):
    def __init__(self, c_type, data, name, color, w_unit="Hz", mod_unit="dB", ph_unit="°"):
        super().__init__(c_type, data, name, color)

        self.w = []
        self.mod = []
        self.ph = []
        self.w_unit = w_unit        # Unidad de la frecuencia, se asume Hz
        self.mod_unit = mod_unit    # Unidad del módulo, se asume dB
        self.ph_unit = ph_unit      # Unidad de la fase, se asume °

    def plot_curve_mod(self, ax):
        ls = get_ls(self.type)
        if ls == '':
            print("Hubo un error, no se puede graficar la curva")
            return False
        if self.type != 4:
            ax.semilogx(self.w, self.mod, self.color, marker=ls)  # Grafico el módulo de la transferencia
        else:
            for i in range(len(self.w)):
                ax.semilogx(self.w[i], self.mod[i], self.color, marker=ls)  # Grafico el módulo de la transferencia
        return True

    def plot_curve_ph(self, ax):
        ls = get_ls(self.type)
        if ls == '':
            print("Hubo un error, no se puede graficar la curva")
            return False
        if self.type != 4:
            ax.semilogx(self.w, self.ph, self.color, marker=ls)  # Grafico el módulo de la transferencia
        else:
            for i in range(len(self.w)):
                ax.semilogx(self.w[i], self.ph[i], self.color, marker=ls)  # Grafico la fase de la transferencia
        return True

    # change_w_unit: Cambia la unidad de la frecuencia de Hz a rad/s o viceversa
    # Si no se especifica la unidad a la que se quiere cambiar o es una que no existe, hace un switch
    def change_w_unit(self, unit=""):
        if unit == "rad/seg" or unit == "rad/s":
            unit = "\\frac{rad}{s}"
        if self.w_unit != unit:
            if self.w_unit == "Hz":
                self.w_unit = "\\frac{rad}{s}"
                self.w = 2*np.pi*self.w
            else:
                self.w_unit = "Hz"
                self.w = self.w/(2*np.pi)
        return

    # change_mod_unit: Cambia la unidad del módulo de dB a ?? o viceversa
    # Si no se especifica la unidad a la que se quiere cambiar o es una que no existe, hace un switch
    def change_mod_unit(self, unit=""):
        if self.mod_unit != unit:
            if self.mod_unit == "dB":
                self.mod_unit = "veces"
                self.mod = np.power(10, self.mod/20)
            else:
                self.mod_unit = "dB"
                self.mod = 20*np.log10(self.mod)
        return

    # change_ph_unit: Cambia la unidad de la fase de ° a rad o viceversa
    # Si no se especifica la unidad a la que se quiere cambiar o es una que no existe, hace un switch
    def change_ph_unit(self, unit=""):
        if self.ph_unit != unit:
            if self.ph_unit == "°":
                self.ph_unit = "rad"
                self.ph = np.pi*self.ph/180
            else:
                self.ph_unit = "°"
                self.ph = 180*self.ph/np.pi
        return
########################################################################################################################

########################################################################################################################
# Clase Teo: Curva teórica, hija de la clase Curve
# Tiene algunos parámetros extra:
#       - H: Función Transferencia (scipy)
# ----------------------------------------------------------------------------------------------------------------------
class Teo(FrecCurve):
    def __init__(self, c_type, data, name, color, w_unit="rad/seg", mod_unit="dB", ph_unit="°"):
        super().__init__(1, data, name, color, w_unit, mod_unit, ph_unit)
        num, den = self.check_data(self.rawdata)
        self.H = None
        if num is not None and den is not None:         # Si están en orden, hace la modificación
            self.H = ss.TransferFunction(num, den)
            self.w, self.mod, self.ph = ss.bode(self.H)
            if self.w_unit == "Hz":
                self.w = self.w/(2*np.pi)

    # change_data: Revisa la validez de los datos nuevos.
    # Devuelve False si hubo error.
    def change_data(self, data):
        r = True
        num, den = self.check_data(self.rawdata)        # Revisa los datos nuevos
        if num is not None and den is not None:         # Si están en orden, hace la modificación
            self.H = ss.TransferFunction(num, den)
            self.w, self.mod, self.ph = ss.bode(self.H)
        else:
            print("Los datos ingresados no son válidos")
            r = False
        return r

    # check_data: Procesa los datos de la función transferencia, asume que se recibe un arreglo con el numerador y denominador como strings
    # Ej data = ["1, 2,1, ,5", "3, 4, 1,3"]
    # Los espacios de más se eliminan y los números racionales se ingresan con punto (1.5)
    # Devuelve num = None y den = None si hubo error
    def check_data(self, data):
        num = fix_coefs(data[0])
        den = fix_coefs(data[1])

        return num, den
########################################################################################################################

########################################################################################################################
# Clase Sim: Curva simulada, hija de la clase Curve
# Tiene unos parámetros extra: - Mentira por ahora no tiene
# w, mod y ph serán [] si hubo error
# ----------------------------------------------------------------------------------------------------------------------
class Sim(FrecCurve):
    def __init__(self, c_type, data, name, color, w_unit="Hz", mod_unit="dB", ph_unit="°"):
        super().__init__(2, data, name, color, w_unit, mod_unit, ph_unit)
        if self.check_file(data):
            self.w, self.mod, self.ph = self.check_data(self.rawdata)

    # change_data: Setter para los datos
    # Devuelve False si hubo error
    def change_data(self, path):
        r = False
        if self.check_file(path):
            self.rawdata = path
            self.w, self.mod, self.ph = self.check_data(self.rawdata)
            r = True
        return r

    # check_data: Parsea el txt de la simulación de LTSpice, asume que tiene el formato de los ejemplos
    # Devuelve w, mod, ph
    def check_data(self, path):
        file = open(path, "r")
        file.readline()
        aux = file.readline().split("\t")
        aux_mod, aux_ph = aux[1][1:-2].split(",")
        count = 2

        self.mod_unit = get_unit(aux_mod)
        self.ph_unit = get_unit(aux_ph)
        for line in file:
            if line != "\n":
                count += 1
        file.close()

        w = np.zeros(count - 1)
        mod = np.zeros(count - 1)
        ph = np.zeros(count - 1)

        l = open(path, "r")

        l.readline()
        for i in range(count - 1):
            aux = l.readline().split("\t")
            w[i] = aux[0]
            aux_mod, aux_ph = aux[1][1:-2].split(",")
            mod[i] = aux_mod.replace(self.mod_unit, "")
            ph[i] = aux_ph.replace(self.ph_unit, "")
        l.close()

        if self.ph_unit == 'Â°': self.ph_unit = '°'

        return w, mod, ph

    # check_file: Revisa que el archivo exista, que sea .txt y que tenga el formato adecuado
    # Devuelve False en caso de error
    def check_file(self, path):
        r = True
        ext = os.path.splitext(path)[1]
        if self.type == 2 and ext != ".txt":
            print("El archivo de la simulación no está en formato .txt")
            r = False
            return r
        if not os.path.isfile(path):
            print("El archivo no existe")
            r = False
        else:
            if not os.access(path, os.R_OK):
                print("El archivo no es legible")
                r = False
            else:
                file = open(path, "r")
                if len(file.readline().split("\t")) != 2:
                    print("El archivo no cumple con el formato adecuado")
                    r = False
        return r
########################################################################################################################

########################################################################################################################
# Clase Med: Curva medida, hija de la clase Curve
#   Tiene unos parámetros extra: - Mentira por ahora no tiene
# ----------------------------------------------------------------------------------------------------------------------
class Med(FrecCurve):
    def __init__(self, c_type, data, name, color, w_unit="Hz", mod_unit="dB", ph_unit="°"):
        super().__init__(3, data, name, color, w_unit, mod_unit, ph_unit)
        if self.check_file(data):
            self.w, self.mod, self.ph = self.check_data(self.rawdata)

    # change_data: Setter para los datos
    # Devuelve False si hubo error
    def change_data(self, path):
        r = False
        if self.check_file(path):
            self.rawdata = path
            self.w, self.mod, self.ph = self.check_data(self.rawdata)
            r = True
        return r

    # check_data: Parsea el csv de la medición de la Digilent, asume que tiene el formato de los ejemplos
    # Devuelve w, mod, ph
    def check_data(self, path):
        file = open(path, "r")
        count = 0
        for line in file:
            if line != "\n":
                count += 1
        file.close()

        w = np.zeros(count - 1)
        mod = np.zeros(count - 1)
        ph = np.zeros(count - 1)

        l = open(path, "r")

        aux = l.readline()
        units = []
        for i in range(3):
            j1 = aux.find("(")
            j2 = aux.find(")")
            units.append(aux[j1 + 1: j2])
            aux = aux[j2 + 1:]
        self.w_unit = units[0]
        self.mod_unit = units[1]
        if units[2] == "deg":
            self.ph_unit = "°"

        for i in range(count - 1):
            aux = l.readline().split(",")
            w[i] = aux[0]
            mod[i] = aux[1]
            ph[i] = aux[2]
        l.close()

        return w, mod, ph

    # check_file: Revisa que el archivo exista, sea .csv y que tenga el formato adecuado
    # Devuelve False en caso de error
    def check_file(self, path):
        r = True
        ext = os.path.splitext(path)[1]
        if self.type == 3 and ext != ".csv":
            print("El archivo de la medición no está en .csv")
            r = False
            return r
        if not os.path.isfile(path):
            print("El archivo no existe")
            r = False
        else:
            if not os.access(path, os.R_OK):
                print("El archivo no es legible")
                r = False
            else:
                file = open(path, "r")
                if len(file.readline().split(",")) != 3:
                    print("El archivo no cumple con el formato adecuado")
                    r = False
        return r
########################################################################################################################

########################################################################################################################
# Clase MC: Simulación de Monte Carlo, hija de la clase Curve
# Tiene unos parámetros extra: - Mentira por ahora no tiene
# w, mod y ph serán [] si hubo error
# ----------------------------------------------------------------------------------------------------------------------
class MC(FrecCurve):
    def __init__(self, c_type, data, name, color, w_unit="Hz", mod_unit="dB", ph_unit="°"):
        super().__init__(4, data, name, color, w_unit, mod_unit, ph_unit)
        if self.check_file(data):
            self.w, self.mod, self.ph = self.check_data(self.rawdata)

    # change_data: Setter para los datos
    # Devuelve False si hubo error
    def change_data(self, path):
        r = False
        if self.check_file(path):
            self.rawdata = path
            self.w, self.mod, self.ph = self.check_data(self.rawdata)
            r = True
        return r

    # check_data: Parsea el txt de la simulación de LTSpice, asume que tiene el formato de los ejemplos
    # Devuelve w, mod, ph
    def check_data(self, path):
        file = open(path, "r")
        file.readline()
        aux = file.readline()
        j1 = aux.find("/")
        j2 = aux.find(")")
        runs = int(aux[j1 + 1: j2])
        aux = file.readline().split("\t")
        aux_mod, aux_ph = aux[1][1:-2].split(",")

        count = 2
        self.mod_unit = get_unit(aux_mod)
        self.ph_unit = get_unit(aux_ph)
        for line in file:
            if line != 'Step Information: Run=2  (Run: 2/' + str(runs) + ')\n':
                count += 1
            else:
                break
        file.close()

        w = np.zeros((runs, count - 1))
        mod = np.zeros((runs, count - 1))
        ph = np.zeros((runs, count - 1))

        l = open(path, "r")

        l.readline()
        for k in range(runs):
            l.readline()
            for i in range(count - 1):
                aux = l.readline().split("\t")
                w[k][i] = aux[0]
                aux_mod, aux_ph = aux[1][1:-2].split(",")
                mod[k][i] = aux_mod.replace(self.mod_unit, "")
                ph[k][i] = aux_ph.replace(self.ph_unit, "")
        l.close()

        if self.ph_unit == 'Â°': self.ph_unit = '°'

        return w, mod, ph

    # check_file: Revisa que el archivo exista, que sea .txt y que tenga el formato adecuado
    # Devuelve False en caso de error
    def check_file(self, path):
        r = True
        ext = os.path.splitext(path)[1]
        if self.type == 2 and ext != ".txt":
            print("El archivo de la simulación no está en formato .txt")
            r = False
            return r
        if not os.path.isfile(path):
            print("El archivo no existe")
            r = False
        else:
            if not os.access(path, os.R_OK):
                print("El archivo no es legible")
                r = False
            else:
                file = open(path, "r")
                if len(file.readline().split("\t")) != 2:
                    print("El archivo no cumple con el formato adecuado")
                    r = False
                elif file.readline().find('Step Information: Run=1') == -1:
                    print("El archivo no cumple con el formato adecuado")
                    r = False
        return r
########################################################################################################################

########################################################################################################################
# fix_coefs: Acomoda los coeficientes del numerador o denominador y revisa si están bien ingresados
#            Devuelve None en caso de error
# ----------------------------------------------------------------------------------------------------------------------
def fix_coefs(coefs):
    r = True
    coefs = coefs.replace(" ", "")  # Elimina espacios
    if coefs == "":
        r = False
        print("Por favor ingrese los coeficientes")
    coefs = coefs.replace(",,", ",0,")
    if coefs[0] == ",":
        coefs = coefs[1:]
    if coefs[-1] == ",":
        coefs = coefs + "0"
    coefs = coefs.split(",")
    try:
        coefs = [float(s) for s in coefs]
    except ValueError:
        print("Uno de los valores ingresados no es numérico")
        r = False
    if not r:
        coefs = None
    return coefs
########################################################################################################################

########################################################################################################################
#   get_unit: Obtiene la unidad de los datos simulados de la curva
# ----------------------------------------------------------------------------------------------------------------------
def get_unit(s):
    unit = ""
    for i in range(len(s) - 1, 0, -1):
        if not s[i].isdigit():
            unit = s[i] + unit
            # s = s[:i]
        else:
            break
    return unit
########################################################################################################################

########################################################################################################################
# get_ls: Obtiene el linestyle correcto para graficar según el tipo de curva
def get_ls(type):
    if type == 2 or type == 1 or type == 4:
        ls = ','
    elif type == 3:
        ls = '.'
    else:
        ls = ''
    return ls
########################################################################################################################


