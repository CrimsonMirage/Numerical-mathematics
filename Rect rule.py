# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:21:39 2020

@author: Danny
"""

from fractions import Fraction
node0 = 0
node1 = 1/3
node2 = 2/3
node3 = 1
f0 = 1/8
f1 = 1/7
f2 = 1/4
f3 = 1
h = node1-node0
def rect(f0,f1,f2,f3,h):
    integralr = h*(f0+f1+f2)
    print(Fraction(integralr).limit_denominator(10000))
    return
def trapezoidal(f0,f1,f2,f3,h):
    integralt = h*((f0/2)+f1+f2+(f3/2))
    print(Fraction(integralt).limit_denominator(10000))
    return
rect(f0,f1,f2,f3,h)
trapezoidal(f0,f1,f2,f3,h)
    
