#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script con diferentes funciones para graficar los resultados de Burgers 2D. 
Se puede usar como ejemplo para algunas graficas futuras. 
@author: toni
"""

# ==============================================================================
# Funcion que grafica la señal en profundidades seleccionadas
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt

def damping(vec, steps, zsel, name):
    
    u2 = np.ceil(np.amax(vec))
    if np.floor(np.amin(vec)) < 0:
        u3 = np.floor(np.amin(vec))
    else: 
        u3 = 0.
    
    f1, axarr = plt.subplots(len(zsel), 1, sharey=True, sharex=True)
  
    for i in range(0, len(zsel)):
        
        axarr[i].plot(steps, vec[len(zsel) - i - 1,:])

        axarr[i].set_yticklabels(np.linspace(u3, u2, 3), fontsize=7.5) 
        axarr[i].set_xticklabels(np.linspace(0, 120, 7), fontsize = 8.5)
        axarr[i].set_aspect('auto')
        axarr[i].grid(True)
        
        if i == 0:
            axarr[i].set_title(name + r'$(cm/s)$', fontsize=10)
            plt.ylim((u3, u2))
            plt.xlim((0, 120))
                    
    plt.tight_layout(h_pad=0.5)  
    plt.savefig(name + '.pdf')
    plt.show()

    return(f1, axarr)

# ==============================================================================
# Función para graficar ventana de tiempo seleccionada de acuerdo con 
# requerimientos (verificación de datos)
# ==============================================================================

def damping2(vec, steps, zsel, name):
    
    ventana = 1500
    limite = ventana * 1e-2
    
    u2 = np.ceil(np.amax(vec))
    if np.floor(np.amin(vec)) < 0:
        u3 = np.floor(np.amin(vec))
    else: 
        u3 = 0.
    
    f1, axarr = plt.subplots(len(zsel), 1, sharey=True, sharex=True)
  
    for i in range(0, len(zsel)):
        
        axarr[i].plot(steps[0:ventana], vec[len(zsel) - i - 1,0:ventana])

        axarr[i].set_yticklabels(np.linspace(u3, u2, 3), fontsize=7.5) 
        axarr[i].set_xticklabels(np.linspace(0, limite, 7), fontsize = 8.5)
        axarr[i].set_aspect('auto')
        axarr[i].grid(True)
        
        if i == 0:
            axarr[i].set_title(name + r'$(cm/s)$', fontsize=10)
            plt.ylim((u3, u2))
            plt.xlim((0, limite))
                    
    plt.tight_layout(h_pad=0.5)  
    plt.savefig(name + str(2) + '.pdf')
    plt.show()
    
    return(f1, axarr)