from matplotlib.colors import is_color_like
 
########################################################################################################################
# Clase Curvespace: Contiene la lista de curvas y métodos para modificarla (Template)
# # ----------------------------------------------------------------------------------------------------------------------
class Curvespace:
    def __init__(self):
        self.curves = []        # Arreglo de curvas

    # update: Método para actualizar los valores de la curva sin tener que borrarla y crearla de vuelta
    # OJO: En vez de recibir el tipo de curva, recibe el índice
    def update(self, index, data, name="", color=""):
        self.change_curve_name(index, name)
        self.change_curve_color(index, color)
        self.curves[index].change_data(data)
        return

    # addCurve: Método para agregar una curva. Para más detalles mirar clase Curva
    def add_curve(self, c_type, data, name="", color=""):
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
        return

    # delCurve: Saca la curva del Curvespace y la destruye
    # Recibe la curva (elemento) (Lo puedo cambiar al índice o nombre, lo que resulte más cómodo)
    def del_curve(self, c):
        self.curves.remove(c)
        del c
        return

    # get_names: Devuelve un arreglo con los nombres de las curvas
    # Si se especifica el parámetro v=True, sólo devolverá los nombres de las curvas visibles
    def get_names(self, v=False):
        names = []
        for i in range(len(self.curves)):
            if not v or self.curves[i].visibility:
                names.append(self.curves[i].name)
        return names

    # check_name: Revisa si el nombre que se quiere asignar ya existe
    # Devuelve False si ya existe, True si está disponible
    def check_name(self, name):
        r = True
        for i in range(len(self.curves)):
            if name == self.curves[i].name:
                r = False
                print("El nombre que quiere asignar ya existe")
                break
        return r

    # change_curve_name: Setter para el nombre de una curva. Recibe:
    #   - index: índice de la curva en el arreglo (lo puedo cambiar a nombre o a la curva en sí lo que les resulte más cómodo)
    #   - name: nombre nuevo para la curva
    # Devuelve False en caso de error (el nuevo nombre ya está asignado)
    def change_curve_name(self, index, name):
        r = self.check_name(name)
        if name != "" and r: self.curves[index].name = name
        else: print("Se mantendrá el nombre anterior")
        return r

    # change_curve_color: Setter para el color de una curva. Recibe:
    #   - index: índice de la curva en el arreglo
    #   - color: color nuevo para la curva
    # Devuelve False en caso de error
    def change_curve_color(self, index, color):
        r = True
        if color == "" or not is_color_like(color):
            print("Se mantendrá el color " + self.curves[index].color)
            r = False
        else:
            self.curves[index].color = color
        return r
########################################################################################################################

########################################################################################################################
# Clase Curve: Contiene toda la información para graficar la curva. Necesita:
#    - Tipo de curva: Dependerá de si es en tiempo o frecuencia
#    - Raw Data: Dependerán del tipo de curva, en cada caso se especifica mejor (mirar funciones)
#    - Nombre: Si no se especifica, se le asignará uno según el orden
#    - Color: Se permitirá elegir el color de la curva, si no se especifica se tomará naranja
#    - Visibilidad: True si la curva está visible, False si está oculta
# Para cada tipo se accede una clase particular, mirarlas para más detalles
# ----------------------------------------------------------------------------------------------------------------------
class Curve:
    def __init__(self, c_type, data, name, color, w_unit="Hz", mod_unit="dB", ph_unit="°"):
        self.type = c_type          # Tipo de curva
        self.rawdata = data         # Datos como se cargan
        self.name = name            # Nombre de la curva
        self.color = color          # Color de la curva
        self.visibility = True      # Está visible? Por defecto se inicializa en True

    # change_visibility: Cambia la visibilidad
    def change_visibility(self):
        self.visibility = not self.visibility
        return

    # check_data: Método para la verificación de datos (método virtual)
    def check_data(self, data):
        return

    # change_data: Setter para la modificación de datos (método virtual)
    def change_data(self, data):
        return
########################################################################################################################


