#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:20:03 2017
Funcion para calcular los promedios por columnas de un arreglo cualquiera
Antonio Preziosi-Ribero
Mayo de 2017
@author: toni
"""

import numpy as np

def promedio(A):
    
    x = np.zeros((1, A.shape[1]))
       
    if A.shape[0] > 1:
        
        for i in range(0, A.shape[1]):
            x[0, i] = np.average(A[:,i])
    else: 
        x = A
        
    return(x)