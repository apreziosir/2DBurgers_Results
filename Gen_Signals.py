# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:08:57 2017

@author: toni
"""

# Programa para extraer señales de velocidad, analizarlas y graficarlas

import numpy as np

# Archivos a leer con sus rutas
# fpath = '/media/toni/Apollo M100 USB3/Doctorado/Modelos/Burgers_2D/05_Nomralized/'
fpath = '/home/toni/Documents/'
folder = '01_Preliminary/'
fname = 'ZBurgers_'
ext = '.dat'
f1 = fpath + folder + fname

# Variables de entrada
puntos      = 5000
tsteps      = 10                             # Pasos de tiempo
xsel        = np.array([10., 20., 30.])     # Lineas de muestreo
zsel        = np.array([0., -0.625, -1.25, -2.5, -5., -10., -15., -18.75, -20.])

# Generando arreglo de almacenamiento de resultados
coords = np.zeros([puntos, 2])
u_raw = np.zeros([puntos, tsteps])
w_raw = np.zeros([puntos, tsteps])
uu_raw = np.zeros([puntos, tsteps])
ww_raw = np.zeros([puntos, tsteps])
uw_raw = np.zeros([puntos, tsteps])

# Cargando coordenadas al arreglo 
coords = np.loadtxt(fpath + folder + fname + str(11).zfill(4) + ext, 
                    skiprows = 3, usecols=(0, 1))

# Loop sobre pasos de tiempo considerados
for i in range(0, tsteps):
    f2 = f1 + str(i + 10).zfill(4) + ext
    u_raw[:, i] = np.loadtxt(f2, skiprows = 3, usecols=[2])
    w_raw[:, i] = np.loadtxt(f2, skiprows = 3, usecols=[3])
    uu_raw[:, i] = np.loadtxt(f2, skiprows = 3, usecols=[4])
    ww_raw[:, i] = np.loadtxt(f2, skiprows = 3, usecols=[5])
    uw_raw[:, i] = np.loadtxt(f2, skiprows = 3, usecols=[6])
    
# Extrayendo arreglos para cada uno de los x analizados
x1 = 
x2 = 
x3 =  

