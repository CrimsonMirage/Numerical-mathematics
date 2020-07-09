# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:48:56 2020

@author: Danny
"""
import numpy as np
import time
start_time = time.time()

def function(x):
    #x=0.0000000000001 if x==0 else x
    val = x**2
    return val
def rectrule(intervalleft, intervalright, h):
    rect=0
    n = (intervalright - intervalleft)/h
    for i in range(int(n)):
        #print(i*h)
        rect = rect + function(intervalleft+i*h)*h
        #print(rect)
    return rect
def trapezrule(intervalleft, intervalright, h):
    trap=0
    n=(intervalright - intervalleft)/h
    for i in range(int(n)):
        trap = trap + (function(intervalleft+i*h)+function(intervalleft+(i+1)*h))*h/2
    return trap
def midprule(intervalleft, intervalright,h):
    midp = 0
    n= (intervalright - intervalleft)/h
    for i in range(int(n)):
        midp = midp + function((intervalleft+i*h+intervalleft+(i+1)*h)/2)*h
    return midp
def simpsonrule(intervalleft, intervalright, h):
    simps = 0
    n = (intervalright - intervalleft)/h
    for i in range(int(n)):
        simps = simps + (h/6)*(function(intervalleft+i*h)+4*function((intervalleft+i*h+intervalleft+(i+1)*h)/2)+function(intervalleft+(i+1)*h))
    return simps
intervalleft = 0
intervalright = 1
steps = 3
h = (intervalright-intervalleft)/steps
#print(h)
rectangle = rectrule(intervalleft, intervalright, h)
trapezoid = trapezrule(intervalleft, intervalright, h)
midpoint = midprule(intervalleft, intervalright,h)
simpson = simpsonrule(intervalleft, intervalright,h)
print(rectangle)
print(trapezoid)
print(midpoint)
print(simpson)
print("--- %s seconds ---" % (time.time() - start_time))