# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:33:34 2020

@author: Danny
"""
import numpy as np
from sympy.calculus.util import maximum, minimum
from sympy import symbols, Interval, sqrt

def point2linearinterpol(x,x1,x2,f1,f2):
    #x is the point we interpolate at, x1 is begin node, x2 is end node, f1 and f2 and the function values at the specific nodes.
    L = ((x-x2)/(x1-x2))*f1 + ((x-x1)/(x2-x1))*f2 #general form of linear interpolation
    print('Linear interpol is: ', L)
    return L

def lagrangianinterpol(x,x0,x1,x2,f0,f1,f2):
    #Similar to 2point linear interpolation, but now with an extra node, x0.
    L2 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))*f0+((x-x0)*(x-x2))/((x1-x0)*(x1-x2))*f1+((x-x0)*(x-x1))/((x2-x0)*(x2-x1))*f2
    print('Langrangian interpol says: ',L2)
    return L2

def findmax(x0,x2):
    #finds the max of the third derivative of the functions. First we use sympy calculus package to easily take the nth derivative (3 in this case)
    #and then we attempt to find both the maximum and minimum value of this function. Take the absolute value of both of these and spit out the
    #biggest absolute value
    f_prime = functions.diff(xn)
    f_prime2 = f_prime.diff(xn)
    f_prime3 = f_prime2.diff(xn)
    ivl = Interval(x0,x2)
    maxval = maximum(f_prime3, xn, ivl)
    minval = minimum(f_prime3, xn,ivl)
    absmax=max(abs(maxval),abs(minval))
    return absmax

def lagrangianerror(x,x0,x1,x2,maxvalue='false'):
    #find the multiplier, the thingymcthing in front of the the xi (including the factorial), take the max value of the function, multiple and boom
    if maxvalue== 'false':
        maxvalue = findmax(x0,x2)
    multiplier = (x-x0)*(x-x1)*(x-x2)/np.math.factorial(3)
    error=abs(multiplier*(maxvalue))
    print('Langrangian error is: ',error)
    return error

xn=symbols('x') #use xn as a fuction of x
functions = sqrt(xn) #function to interpolate

x = 1 #point of interpolation
x0 = -1 #node 1
x1 = 1 #node 2
x2 = 4 # node 3
givenerror = 0.4210 #if you get an upperbound error, use this

approxlin=point2linearinterpol(x,x1,x2,functions.subs(xn,x0),functions.subs(xn,x2))
approxlag=lagrangianinterpol(x,x0,x1,x2,functions.subs(xn,x0),functions.subs(xn,x1),functions.subs(xn,x2))
interpolationerr = lagrangianerror(x,x0,x1,x2, givenerror) #add ,givenerror behind x2 if upperbound error is given
