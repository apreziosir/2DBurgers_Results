#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from Functions_toni import promedio
import matplotlib.pyplot as plt

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

cont = 0

for i in range(0, len(xsel)):
        
    for j in range(0, len(zsel)):
        
        # Seleccionando la coordenada x 
        u_prueba = u_raw[u_raw[:,0] == xsel[i]]
        w_prueba = w_raw[w_raw[:,0] == xsel[i]]
        uu_prueba = uu_raw[uu_raw[:,0] == xsel[i]]
        ww_prueba = ww_raw[ww_raw[:,0] == xsel[i]]
        uw_prueba = uw_raw[uw_raw[:,0] == xsel[i]]
        
        # Seleccionando la coordenada z
        u_prueba = u_prueba[u_prueba[:,1] == zsel[j]]
        w_prueba = w_prueba[w_prueba[:,1] == zsel[j]]
        uu_prueba = uu_prueba[uu_prueba[:,1] == zsel[j]]
        ww_prueba = ww_prueba[ww_prueba[:,1] == zsel[j]]
        uw_prueba = uw_prueba[uw_prueba[:,1] == zsel[j]]
        
        # Calculando el promedio de las columnas de las selecciones
        u_sel[cont,:] = promedio(u_prueba)
        w_sel[cont,:] = promedio(w_prueba)
        uu_sel[cont,:] = promedio(uu_prueba)
        ww_sel[cont,:] = promedio(ww_prueba)
        uw_sel[cont,:] = promedio(uw_prueba)
        
        # Borrando los arreglos de prueba para volver a iterar
        del(u_prueba, w_prueba, uu_prueba, ww_prueba, uw_prueba)
        
        # Actualizando valor del contador
        cont += 1        
        
# Graficando señales de velocidad en profundidades seleccionadas (u)
f, axarr = plt.subplots(len(zsel), 1)

for i in range(0, len(zsel)):
    axarr[i, 0].plot(steps, u_sel[i, 2:pasos])
    if i == 0:
        axarr[i, 0].set_title(r'\Velocity damping $cm/s$')

## Fine-tune figure; hide x ticks for top plots and y ticks for right plots
#plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

plt.show()