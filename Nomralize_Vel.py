# -*- coding: utf-8 -*-
"""
Spyder Editor
Script para dar valores normalizados de velocidad a los datos extraidos del 
modelo LES de Northwestern (después de filtrarlos y ordenarlos)
Antonio Preziosi-Ribero, Mayo de 2017
"""

# Librerias necesarias
import numpy as np

# Variables de entrada del script
rpath = '/home/toni/Documents/2DBurgers/Filtered/'
fname = 'Filt_vel.csv'
wname = 'Norm_vel.csv'
wpath = '/home/toni/Documents/2DBurgers/Normalized/'
nof =  16757
puntos = 100

# Construccion de arreglos de almacenamiento
u_tot = np.zeros(nof)
w_tot = np.zeros(nof)

# Calculando los totales de velocidad para promedio
for i in range (0, nof):
    arch = rpath + str(i).zfill(5) + fname
    x = np.loadtxt(arch)
    u_tot[i] = np.sum(x[:,0])
    w_tot[i] = np.sum(x[:,1])
    del x
    
# Calculando valores medios del ensamble de velocidades
U_mean = np.sum(u_tot) / (nof * puntos)
W_mean = np.sum(w_tot) / (nof * puntos)

# Deleting arrays of totals (memory purposes)
del(u_tot, w_tot)

# Constructing files with fluctuations of velocity instead of total values
for i in range(0, nof + 1):
    arch = rpath + str(i).zfill(5) + fname
    x = np.loadtxt(arch)
    x[:,0] = x[:,0] - U_mean
    x[:,1] = x[:,1] - W_mean
    arche = wpath + str(i).zfill(5) + wname
    np.savetxt(arche, x, newline='\n')
    del x   