import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss
#from backend import Curvespace
from frecspace import Frecspace
from timespace import Timespace

# ARCHIVO PARA PROBAR LAS FUNCIONALIDADES DEL BACKEND ANTES DE AGREGAR EL FRONT

# TEST
CS = Frecspace()
TS = Timespace()
#CS.add_curve(1, ["1", "1, 2"])
w_0 = 2*np.pi*10.8E3
# CS.add_curve(1, ["-1E11", "1, 2E6, 1E12"], name="Prueba")
CS.add_curve(1, [f"{w_0**-2}, 0, 1", f"{w_0**-2}, {4/w_0}, 1"], name="Teórica", color="mediumblue", w_unit="Hz", mod_unit="dB", ph_unit="°")
CS.add_curve(2, "Rta_Frecruencia.txt", name="Simulada", color="orange", w_unit="Hz", mod_unit="dB", ph_unit="°")
#CS.add_curve(4, "montecarlo-simulacion.txt", name="Montecarlo 4", color="violet")
#CS.add_curve(4, "montecarlo2-simulacion.txt", name="Montecarlo 2")
#C = 68E-9
#R = 2.2E2
TS.add_curve(2, [CS.curves[0], np.linspace(0, 300E-6, 1000), [1.0]], name="Teórica", color="mediumblue", t_unit="s", y_unit="V")
TS.add_curve(0, "Rta_Escalon.txt", name="Simulada", color="orange", t_unit="s", y_unit="V")
TS.change_t_unit("ms")
#TS.change_y_unit("\\mu V")
#CS.add_curve(2, "D:\Descargas\Rta_Frecruencia.txt", name="Simulada", color="orange")
#CS.add_curve(3, "Ejemplo1-medicion.csv", name="Prueba")
'''C.change_curve_name(1, "Pitusas")
C.curves[2].change_ph_unit()
C.change_w_unit("rad/s")
C.change_x_mod_label("w")
C.change_x_ph_label("Frecuencia")'''

fig, ax = plt.subplots(1)
#fig, ax = plt.subplots(2, 1)
fig.suptitle(CS.title)
#CS.plot_mod(ax[0])
CS.plot_ph(ax)#[1])
fig.tight_layout()
plt.savefig(CS.title + ".jpg", dpi=300)
plt.show()

fig2, ax2 = plt.subplots(1)
TS.change_title("Respuesta al escalón")
TS.plot_time(ax2)
fig2.tight_layout()
plt.savefig(TS.title + ".jpg", dpi=300)
plt.show()

'''
def check_data():
    data = "Ejemplo1-simulacion.txt"
    file = open(data, "r")
    count = 2
    w_name, V_name = file.readline().split("\t")
    aux = file.readline().split("\t")
    aux_mod, aux_ph = aux[1][1:-2].split(",")

    mod_unit = get_unit(aux_mod)
    ph_unit = get_unit(aux_ph)
    for line in file:
        if line != "\n":
            count += 1
    file.close()

    w = np.zeros(count - 1)
    mod = np.zeros(count - 1)
    ph = np.zeros(count - 1)

    l = open(data, "r")

    l.readline()
    for i in range(count - 1):
        aux = l.readline().split("\t")
        w[i] = aux[0]
        aux_mod, aux_ph = aux[1][1:-2].split(",")
        mod[i] = aux_mod.replace(mod_unit, "")
        ph[i] = aux_ph.replace(ph_unit, "")

    l.close()

    return w, mod, ph
'''
def get_unit(s):
    unit = ""
    for i in range(len(s)-1, 0, -1):
        if not s[i].isdigit():
            unit = s[i] + unit
            # s = s[:i]
        else: break
    return unit
'''
w, mod, ph = check_data()
for i in range(len(w)):
    print(w[i], mod[i], ph[i])
'''
'''
# TEST
a = "dB"
fig, ax = plt.subplots(2, 1)
fig.suptitle("Bode plot")
ax[0].semilogx(w, mod)  # Grafico bode del módulo de la transferencia
ax[0].set_xlabel("$\omega$ $\\left[\\frac{rad}{s}\\right]$")
ax[0].set_ylabel("$|H(S)|$ $[" + a + "]$")
ax[0].grid()
ax[1].semilogx(w, ph)  # Grafico bode de la fase de la transferencia
ax[1].set_xlabel("$\omega$ $\\left[\\frac{rad}{s}\\right]$")
ax[1].set_ylabel("$\phi(H(s))$ $[°]$")
ax[1].grid()
fig.tight_layout()
plt.show()
'''

'''
def check_mc_data(path):
    file = open(path, "r")
    file.readline()
    aux = file.readline()
    j1 = aux.find("/")
    j2 = aux.find(")")
    runs = int(aux[j1 + 1: j2])
    aux = file.readline().split("\t")
    aux_mod, aux_ph = aux[1][1:-2].split(",")

    count = 2
    mod_unit = get_unit(aux_mod)
    ph_unit = get_unit(aux_ph)
    for line in file:
        if line != 'Step Information: Run=2  (Run: 2/100)\n':
            count += 1
        else: break
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
            mod[k][i] = aux_mod.replace(mod_unit, "")
            ph[k][i] = aux_ph.replace(ph_unit, "")
    l.close()

    if ph_unit == 'Â°': ph_unit = '°'

    return w, mod, ph

import os
def check_file(path):
    r = True
    ext = os.path.splitext(path)[1]
    if ext != ".txt":
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
            elif file.readline() != 'Step Information: Run=1  (Run: 1/100)\n':
                print("El archivo no cumple con el formato adecuado")
                r = False
    return r

if check_file("montecarlo-simulacion.txt"):
    w, mod, ph = check_mc_data("montecarlo-simulacion.txt")
    for i in range(len(w[0])):
        print(w[16][i], mod[16][i], ph[16][i])
    print(len(w[0]))
'''
