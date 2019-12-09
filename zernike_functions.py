# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 13:16:35 2019

@author: Tom Smart
"""

import math

def zernike_radial(rho = 0, n = 0, m = 0):
    s = 0
    R = 0
    while s <= (n - abs(m)) / 2:
        R = R + ((-1)^s * math.factorial(n-s)) / (math.factorial(s) * math.factorial(0.5 * (n + abs(m)) - s) * math.factorial(0.5 * (n - abs(m)) - s)) * rho^(n-2*s);
        s += 1
    return R
        
def zernike_normalisation(n = 0, m = 0):
    if m == 0:
        delta = 1
    else:
        delta = 0
    N = math.sqrt((2 * (n + 1)) / (1 + delta))
    return N
        
def zernike_polynomial(rho = 0, theta = 0, R = 0, N = 0, m = 0, n = 0):
    if m >= 0:
        Z = N * R * math.cos(m * theta)
    elif m < 0:
        Z = -N * R * math.sin(m * theta)
    return Z
    
    