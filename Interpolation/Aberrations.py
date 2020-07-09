# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:35:25 2020

@author: Danny
"""
from sympy import * 
xn, x0,x1,x2,x3 = symbols('xn, x0 x1 x2 x3')

def function(x):
#    if (x==-1):
#        y=3
#    elif (x==0):
#        y=5
#    elif (x==2):
#        y=2
#    elif (x==3):
#        y=3
#    return y #given variables
    return (1/(1+x**2)) #given function

def Laginterpol1(xa,xb):
    #linear interpolation if we only use 1 node
    L1=function(xa)*((xn-x1)/(x0-x1)) +function(xb)*((xn-x0)/(x1-x0))
    return L1

def Laginterpol2(xa,xb,xc):
    #lagrangian interpolation for two nodes
    L2=(function(xa)*(((xn-x1)*(xn-x2))/((x0-x1)*(x0-x2))))+(
            function(xb)*(((xn-x0)*(xn-x2))/((x1-x0)*(x1-x2))))+(
                function(xc)*(((xn-x0)*(xn-x1))/((x2-x0)*(x2-x1))))
    return L2

def Laginterpol3(xa,xb,xc,xd):
    #absolute unit of an interpolation for three nodes
    L3=(function(xa)*(((xn-x1)*(xn-x2)*(xn-x3))/((x0-x1)*(x0-x2)*(x0-x3))))+(
            function(xb)*(((xn-x0)*(xn-x2)*(xn-x3))/((x1-x0)*(x1-x2)*(x1-x3))))+(
                    function(xc)*(((xn-x0)*(xn-x1)*(xn-x3))/((x2-x0)*(x2-x1)*(x2-x3))))+(
                            function(xd)*(((xn-x0)*(xn-x1)*(xn-x2))/((x3-x0)*(x3-x1)*(x3-x2))))
    return L3

def gridnodes(istart,iend,n):
    #finds the right gridnodes
    steps.append(istart)
    stepsize = (iend-istart)/n
    nextstep=istart
    for i in range(n):
        nextstep = nextstep+stepsize
        steps.append(nextstep)
    return(steps)
    
istart=-1 #start of interval
iend=3 #end of interval
n=3 #nodes
steps=[]

#nodes = [-1,0,2,3] nodes are given
nodes = gridnodes(istart,iend,n) #equidistant nodes

if n == 1:
    aberrations = Laginterpol1(nodes[0],nodes[1]).subs([(x0,nodes[0]),(x1,nodes[1])])
if n == 2:
    aberrations = Laginterpol2(nodes[0],nodes[1],nodes[2]).subs([(x0,nodes[0]),(x1,nodes[1]),(x2,nodes[2])])
    aberrations = simplify(aberrations)
if n == 3:
    aberrations = Laginterpol3(nodes[0],nodes[1],nodes[2],nodes[3]).subs([(x0,nodes[0]),(x1,nodes[1]),(x2,nodes[2]),(x3,nodes[3])])
    aberrations = simplify(aberrations)
    #aberrations = aberrations.subs(xn,1)
print(aberrations)

