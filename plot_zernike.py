# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 13:58:04 2019

@author: Tom Smart
"""

import zernike_functions as zern_funs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)


n = 2
m = 0
rho = np.linspace(0, 1, 1e3)
theta = np.linspace(0, 2*np.pi, 1e3)
RHO, THETA = np.meshgrid(rho, theta)

N = zern_funs.zernike_normalisation(n, m)
R = zern_funs.zernike_radial(RHO, n, m)
Z = zern_funs.zernike_polynomial(RHO, THETA, N, R, n, m)

plt.subplot(projection = 'polar')
plt.pcolormesh(THETA, RHO, Z)
plt.plot(THETA, RHO, color = 'k', ls = 'none')
plt.show()