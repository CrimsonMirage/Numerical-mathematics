# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:10:05 2020

@author: Danny
"""
import numpy as np
def function(x):
    return np.sin(3*x+3)
def forwarddiff(x,h):
    est = (function(x+h)-function(x))/h
    print('forward difference estimation is:', est)
    return
def backwarddiff(x,h):
    est = (function(x)-function(x-h))/h
    print('Backward difference estimation is:', est)
    return
def centraldiff(x,h):
    est = (function(x+h)-function(x-h))/(2*h)
    print('Central difference estimation is:', est)
    return
x=1
h=0.07
forwarddiff(x,h)
backwarddiff(x,h)
centraldiff(x,h)