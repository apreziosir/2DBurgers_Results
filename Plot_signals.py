#!/usr/bin/env python3

"""
Created on Wed May  3 16:47:30 2017

Programa para creal las graficas iniciales a partir de la carga de un archivo 
generado en el script Gen_Signals.py 
Este programa solamente graficará datos de esta toma para evitar confusiones 
@author: toni
Antonio Preziosi-Ribero
03 may 2017
"""

import numpy as np 
import matplotlib.pyplot as plt
from Functions_toni import promedio
from Plotting_funct import damping

# Importando los arreglo extraidos de los resultados para graficar las señales
# Cambiar las carpetas de acuerdo con los datos que se van a graficar
path1 = '/media/toni/Apollo M100 USB3/Doctorado/Modelos/Burgers_2D/'
path2 = '05_Normalized/01_Preliminary/Python_Res/'
tot_path = path1 + path2 

# ==============================================================================
# Escogiendo las secciones que se van a hacer para extraer los datos
# Estos arreglos se pueden modificar de acuerdo con las necesidades 
# graficas que tenga el programa
# ==============================================================================
tmax = 119
xsel = np.array([10., 20., 30.])
zsel = np.array([-20., -15., -10., -5., -2.5, -1.25, -0.625, 0.])

# ==============================================================================
# Cargando datos de la carpeta y guardando en arreglos NUMPY
# ==============================================================================
datos = np.load(tot_path + 'compiled.npz')

coords = datos['array6']
u_raw = datos['array1']
w_raw = datos['array2']
uu_raw = datos['array3']
ww_raw = datos['array4']
uw_raw = datos['array5']

del(datos)
puntos = u_raw.shape[0]
pasos = u_raw.shape[1]
steps = np.linspace(0, tmax, u_raw.shape[1])

# ==============================================================================
# Sacando valores medios para poder hacer graficas mas tarde (añadido luego)
# ==============================================================================
u_medias = np.zeros(u_raw.shape[0])
w_medias = np.zeros(w_raw.shape[0])
uu_medias = np.zeros(uu_raw.shape[0])
ww_medias = np.zeros(ww_raw.shape[0])
uw_medias = np.zeros(uw_raw.shape[0])

for i in range(0, u_raw.shape[0]):
    u_medias[i] = np.average(u_raw[i,:])
    w_medias[i] = np.average(w_raw[i,:])
    uu_medias[i] = np.average(uu_raw[i,:])
    ww_medias[i] = np.average(ww_raw[i,:])
    uw_medias[i] = np.average(uw_raw[i,:])

# ==============================================================================
# Armando arreglos con velocidades
# ==============================================================================
u_raw = np.hstack((coords, u_raw))
w_raw = np.hstack((coords, w_raw))
uu_raw = np.hstack((coords, uu_raw))
ww_raw = np.hstack((coords, ww_raw))
uw_raw = np.hstack((coords, uw_raw))

# ==============================================================================
# Creando los arreglos donde se van a almacenar los valores en los puntos 
# seleccionados
# ==============================================================================
u_sel = np.zeros((len(xsel) * len(zsel), u_raw.shape[1]))
w_sel = np.zeros((len(xsel) * len(zsel), u_raw.shape[1]))
uu_sel = np.zeros((len(xsel) * len(zsel), u_raw.shape[1]))
ww_sel = np.zeros((len(xsel) * len(zsel), u_raw.shape[1]))
uw_sel = np.zeros((len(xsel) * len(zsel), u_raw.shape[1]))
coords_sel = np.zeros((len(xsel) * len(zsel), 2))

cont = 0

for i in range(0, len(xsel)):
        
    for j in range(0, len(zsel)):
        
        # Seleccionando la coordenada x 
        u_prueba = u_raw[u_raw[:,0] == xsel[i]]
        w_prueba = w_raw[w_raw[:,0] == xsel[i]]
        uu_prueba = uu_raw[uu_raw[:,0] == xsel[i]]
        ww_prueba = ww_raw[ww_raw[:,0] == xsel[i]]
        uw_prueba = uw_raw[uw_raw[:,0] == xsel[i]]
        coords_prueba = coords[coords[:,0] == xsel[i]]
        
        # Seleccionando la coordenada z
        u_prueba = u_prueba[u_prueba[:,1] == zsel[j]]
        w_prueba = w_prueba[w_prueba[:,1] == zsel[j]]
        uu_prueba = uu_prueba[uu_prueba[:,1] == zsel[j]]
        ww_prueba = ww_prueba[ww_prueba[:,1] == zsel[j]]
        uw_prueba = uw_prueba[uw_prueba[:,1] == zsel[j]]
        coords_prueba = coords_prueba[coords_prueba[:,1] == zsel[j]]
        
        # Calculando el promedio de las columnas de las selecciones
        u_sel[cont,:] = promedio(u_prueba)
        w_sel[cont,:] = promedio(w_prueba)
        uu_sel[cont,:] = promedio(uu_prueba)
        ww_sel[cont,:] = promedio(ww_prueba)
        uw_sel[cont,:] = promedio(uw_prueba)
        coords_sel[cont,:] = promedio(coords_prueba)
        
        # Borrando los arreglos de prueba para volver a iterar
        del(u_prueba, w_prueba, uu_prueba, ww_prueba, uw_prueba, coords_prueba)
        
        # Actualizando valor del contador
        cont += 1        

# Quitando las columnas de coordenadas de los arreglos seleccionados
u_sel = u_sel[:, 2 : pasos + 2]
w_sel = w_sel[:, 2 : pasos + 2]
uu_sel = uu_sel[:, 2 : pasos + 2]
ww_sel = ww_sel[:, 2 : pasos + 2]
uw_sel = uw_sel[:, 2 : pasos + 2]

# ==============================================================================
# Graficas de promedios espaciales de velocidades para las señales con cálculo
# Esto se hace con todos los x... al parecer no es muy refinado. 
# ==============================================================================
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax2 = ax1.twiny()

ax1.plot(u_medias, coords[:, 1], 'red')
ax1.plot(w_medias, coords[:, 1], 'orange')
ax1.set_xlabel(r"Velocity $cm/s$")
ax1.set_ylim(-20, 0.)
ax1.set_xlim(-2., 2)

ax2.plot(uu_medias, coords[:, 1], 'green')
ax2.plot(ww_medias, coords[:, 1], 'blue')
ax2.plot(uw_medias, coords[:, 1], 'purple')
ax2.set_xlim(-2., 2.)
ax2.set_xlabel(r"Velocity stresses $(cm/s)^2$")
plt.savefig('Promedio_todos_puntos.pdf')
plt.show()

# ==============================================================================
# Gráficas espaciales de vlocidades, pero solamente con los x seleccionados
# Es lo mismo que la anterior, pero con emnos puntos para reducir incertidumbre
# ==============================================================================
u_med2 = np.zeros(len(zsel))
w_med2 = np.zeros(len(zsel))
uu_med2 = np.zeros(len(zsel)) 
ww_med2 = np.zeros(len(zsel))
uw_med2 = np.zeros(len(zsel))

for i in range(0, len(zsel)):
    t1 = (1/3) * (np.average(u_sel[i,:]) + np.average(u_sel[i + len(zsel),:]) +
          np.average(u_sel[i + 2 * len(zsel), :]))
    u_med2[i] = t1
    t2 = (1/3) * (np.average(w_sel[i,:]) + np.average(w_sel[i + len(zsel),:]) +
          np.average(w_sel[i + 2 * len(zsel), :]))
    w_med2[i] = t2
    t3 = (1/3) * (np.average(uu_sel[i,:]) + np.average(uu_sel[i + len(zsel),:]) +
          np.average(uu_sel[i + 2 * len(zsel), :]))
    uu_med2[i] = t3
    t4 = (1/3) * (np.average(ww_sel[i,:]) + np.average(ww_sel[i + len(zsel),:]) +
          np.average(ww_sel[i + 2 * len(zsel), :]))
    ww_med2[i] = t4
    t5 = (1/3) * (np.average(uw_sel[i,:]) + np.average(uw_sel[i + len(zsel),:]) +
          np.average(uw_sel[i + 2 * len(zsel), :]))
    uu_med2[i] = t5
    
fig2 = plt.figure()
ax1 = fig2.add_subplot(111)
ax2 = ax1.twiny()

ax1.plot(u_med2, zsel, 'red')
ax1.plot(w_med2, zsel, 'orange')
ax1.set_xlabel(r"Velocity $cm/s$")
ax1.set_ylim(-20, 0.)
ax1.set_xlim(-0.5, 0.5)

ax2.plot(uu_med2, zsel, 'green')
ax2.plot(ww_med2, zsel, 'blue')
ax2.plot(uw_med2, zsel, 'purple')
ax2.set_xlim(-0.5, 0.5)
ax2.set_xlabel(r"Velocity stresses $(cm/s)^2$")
plt.savefig('Promedio_seleccionados.pdf')
plt.show()
    
# Borrando variables que no voy a usar mas (mucho espacio en memoria)
del(cont, u_raw, w_raw, uu_raw, ww_raw, uw_raw)
        
# Graficando señales de velocidad en profundidades seleccionadas
f1, axarr = damping(u_sel, steps, zsel, 'u_damp')
f2, axarr = damping(w_sel, steps, zsel, 'w_damp')
f3, axarr = damping(uu_sel, steps, zsel, 'uu_damp')
f4, axarr = damping(ww_sel, steps, zsel, 'ww_damp')
f5, axarr = damping(uw_sel, steps, zsel, 'uw_damp')



