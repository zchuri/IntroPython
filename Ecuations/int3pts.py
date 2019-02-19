#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:13:56 2019

Find polynomial base on the interpolation of three points:

p(x) = ax^2 + bx + c


@author: churi
"""

#import math
import numpy as np
import matplotlib.pyplot as plt

x1,x2,x3 = 2, 4, 7
y1,y2,y3 = 1, 5, 4


# Find a, b, c
a = (x1*(y3 - y2) + x2*(y1-y3) + x3*(y2-y1))/((x1-x2)*(x1-x3)*(x2-x3))

b = ((y2 - y1)/(x2 - x1)) - a*(x1 + x2)

c = y1 - a*x1**2 - b*x1

# Generate range
z1 = min((x1,x2,x3))
z2 = max((x1,x2,x3))
d = abs(z2 - z1)
x = np.arange(z1 - 0.5*d, z2 + 0.5*d, 0.1)
y = a*x**2 + b*x + c

# Draw
plt.plot(x,y, (x[0],x[len(x)-1]),(0,0))
plt.plot((x1,x2,x3),(y1,y2,y3), "ro")
plt.show()
