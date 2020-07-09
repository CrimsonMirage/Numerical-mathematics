# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:02:23 2020

@author: Danny
"""
import numpy as np
def newtonraphson(p0,itcount=10):
    for i in range(1, itcount):
        pnew=p0-(function(p0)/dfunction(p0))
        p.append(pnew)
        err.append(abs(pnew-(root)))
        p0=pnew
def function(x):
    return (x**2)-16*x
def dfunction(x):
    return 2*x-16
p=[]
p0=2
p.append(p0)
err=[]
root = 0
err.append(abs(p0-root))
newtonraphson(p0)
