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
import matplotlib.pyplot as plt

# Graficando valores medios en profundidad
ax1 = plt.subplot(171)
plt.plot(u_mean, coords[:,1])
plt.setp(ax1.get_yticklabels(), fontsize=8, visible=True)

ax2 = plt.subplot(172, sharex=ax1)
plt.plot(w_mean, coords[:,1])
plt.setp(ax1.get_yticklabels(), visible=False)

ax3 = plt.subplot(173, sharex=ax1)
plt.plot(u_meana, coords[:,1])
plt.setp(ax1.get_yticklabels(), visible=False)

ax4 = plt.subplot(174, sharex=ax1)
plt.plot(w_meana, coords[:,1])
plt.setp(ax1.get_yticklabels(), visible=False)

ax5 = plt.subplot(175, sharex=ax1)
plt.plot(uu_mean, coords[:,1])
plt.setp(ax1.get_yticklabels(), visible=False)

ax6 = plt.subplot(176, sharex=ax1)
plt.plot(ww_mean, coords[:,1])
plt.setp(ax1.get_yticklabels(), visible=False)

ax7 = plt.subplot(177, sharex=ax1)
plt.plot(uw_mean, coords[:,1])
plt.setp(ax1.get_yticklabels(), visible=False)

plt.savefig('Valores_medios.pdf')
plt.show()