# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 13:16:35 2019

@author: Tom Smart
"""

import math
import numpy as np


def zernike_normalisation(n = 0, m = 0):
    """    
    inputs:
    n - radial order
    m - azimuthal frequency
        
    """
    if m == 0:
        delta = 1
    else:
        delta = 0
    N = math.sqrt((2 * (n + 1)) / (1 + delta))
    return N


def zernike_radial(rho = 0, n = 0, m = 0):
    """
    inputs:
    rho - radial coordinate
    n - radial order
    m - azimuthal frequency
    """
    s = 0
    R = 0
    while s <= (n - abs(m)) / 2:
        R += np.multiply(((-1)^s * math.factorial(n-s)) / (math.factorial(s) * math.factorial(0.5 * (n + abs(m)) - s) * math.factorial(0.5 * (n - abs(m)) - s)), np.power(rho, n-2*s))
        s += 1
    return R
        

        
def zernike_polynomial(rho = 0, theta = 0, N = 0, R = 0, n = 0, m = 0):
    """
    inputs:
    rho - radial coordinate
    theta - azimuthal coordinate
    R - radial zernike component
    N - zernike normalisation
    n - radial order
    m - azimuthal frequency
    """
    if m >= 0:
        Z = N * R * np.cos(m * theta)
    elif m < 0:
        Z = -N * R * np.sin(m * theta)
    return Z
    
    