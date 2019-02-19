#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:13:56 2019

Solution to second grade ecuation:

a*x^2 + b*x + c

@author: churi
"""

import math
import numpy as np
import matplotlib.pyplot as plt

a,b,c = 2, 5, 1

print((a,b,c))

dd = b**2 - 4*a*c

if dd < 0:
    print("No root")
else:
    x1 = (-b + math.sqrt(dd)) / (2*a)
    x2 = (-b - math.sqrt(dd)) / (2*a)
    print(("Root 1 = ", round(x1,3)))
    print(("Root 2 = ", round(x2,3)))
    # Generate beautiful plot
    # Generate range
    z1 = min((x1,x2))
    z2 = max((x1,x2))
    d = abs(z2 - z1)
    x = np.arange(z1 - 0.5*d, z2 + 0.5*d, 0.1)
    y = a*x**2 + b*x + c
    # Draw
    plt.plot(x,y, (x[0],x[len(x)-1]),(0,0))
    plt.show()
