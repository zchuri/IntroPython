#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:13:56 2019

Solution to ordinary differential ecuation:

dy/dx = -sin(x) e^2 + y con y(0) = 1

by Euler's method, such as

y(n+1) = y(n) + dt * fn(x, y)


@author: churi
"""

import math
import numpy as np
import matplotlib.pyplot as plt

x1 = 0
y1 = 1
dt = .1
x2 = 3

x = [x1]
y = [y1]

# Numeric solution
while x1 < 3:
    y2 = y1 + dt * (-math.sin(x1) * math.exp(x1) + y1)
    y.append(y2)
    x1 = x1+dt
    y1 = y2
    x.append(x1)

plt.plot(x,y)

# Analitic solution
plt.plot(x, np.cos(x)*np.exp(x))
plt.show()
