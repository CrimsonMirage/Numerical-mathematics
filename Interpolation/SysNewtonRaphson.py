# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:29:23 2020

@author: Danny
"""
import sympy as sp
from sympy import symbols
import numpy as np
x,y = symbols('x y')
variables = sp.Matrix([x,y])


def sysnewtonraphson(n):
    for v in range(n):
        jSysn=np.array((jSys.subs([(x,p[v][0]),(y,p[v][1])])), np.float64)#fill in the variables for p0
        minusF1=np.array((-sys.subs([(x,p[v][0]),(y,p[v][1])])).tolist(),np.float64)
        hn=(np.linalg.solve(jSysn,minusF1))
        pnew =[(p[v][0]+float(hn[0])),p[v][1]+float(hn[1])]
        absvalhn=np.sqrt(hn[0]**2+hn[1]**2)
        print('For n = ',v,'\n using p = ', p[v], '\nOur J(pn) is: ', jSysn)
        print('The -F(pn) is: ', minusF1, '\nour hn is: ', hn,'\n Finally, the length of hn is: ', absvalhn, '\n\n')
        p.append(pnew)
    return p
#Variable declarations
sys = sp.Matrix([2*x**2 + 7*y**2-49, 8*x**2-7*y**2-49]) #systems of equations
jSys = sys.jacobian(variables) #calculate the jacobi matrix
p=[[1,1]]
print('The Jacobi matrix is: ',jSys)
sysnewtonraphson(3)
