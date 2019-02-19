#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:45:53 2019

@author: churi
"""

# Clear workspace
%reset -f

# http://paulbourke.net/fractals/lsys/

# Peano curve
#axiom = X
#X -> XFYFX+F+YFXFY-F-XFYFX
#Y -> YFXFY-F-XFYFX+F+YFXFY
#angle = 90

import turtle

# Initial parameters
axiom = 'F+F+F+F'
fract = ''
rewriting = 'F+F-F-FF+F+F-F'
loops = 2
lax = len(axiom)

# Rewrite fractal variable
for k in range(loops):
    for i in range(lax):
        if axiom[i] == 'F':
            fract = fract+rewriting
        elif axiom[i] == '+':
            fract = fract+axiom[i]
        elif axiom[i] == '-':
            fract = fract+axiom[i]
    axiom = fract
    lax = len(axiom)

# Draw fractal with turtle
fract='F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F-F+F-F-FF+F+F-FF+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F-F+F-F-FF+F+F-FF+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F-F+F-F-FF+F+F-FF+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F-F+F-F-FF+F+F-FF+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F'

lf = len(fract)
#turtle.goto()
turtle.Screen().bye()

turtle.Screen()
turtle.goto(0,0)


for i in range(lf):
    if fract[i] == 'F':
        turtle.forward(5)
    elif fract[i] == '-':
        turtle.right(90)
    elif fract[i] == '+':
        turtle.left(90)

turtle.Screen().bye()

