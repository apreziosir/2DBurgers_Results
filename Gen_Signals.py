# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:08:57 2017

@author: toni
"""

# Programa para extraer señales de velocidad, analizarlas y graficarlas

import numpy as np

# Archivos a leer con sus rutas
fpath = '/media/toni/Apollo M100 USB3/Doctorado/Modelos/Burgers_2D/04_Corrected/'
folder = '170417_znegative/'
fname = 'ZBurgers_'
ext = '.dat'

# Variables de entrada
tsteps      = 839                           # Pasos de tiempo
xsel        = np.array([3.655, 20., 30.])     # Lineas de muestreo
zsel        = np.array([0., -0.625, -1.25, -2.5, -5., -10., -15., -18.75, -20.])

# Generando arreglo de almacenamiento de resultados
u_raw = np.array([tsteps, len(xsel) * len(zsel)])
w_raw = np.array([tsteps, len(xsel) * len(zsel)])

# Loop sobre cadda archivo (paso de tiempo)
for i in range(0, 1):

    # Lectura de archivo de velocidades en tiempo i    
    x = np.loadtxt(fpath + folder + fname + str(i + 10).zfill(4) + ext, 
                   skiprows = 3)

    # Iterando sobre x seleccionado 
    for j in range(0, len(xsel)):
        
        # Extrayendo los valores de x necesarios
        y = x[x[:,0] == 10.]
        