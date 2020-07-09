# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:49:01 2020

@author: Danny
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:07:52 2020

@author: Danny
"""
import numpy as np
A = [[-1,0,0],[6,-4,7],[2,-7,-4]] #given matrix
eigvalues=np.linalg.eigvals(A) #find eigenvalues of the matrix
#print(eigvalues)
lambdalength=[]
def findmax(eigvalues):
    #finds the biggest length of lambda for a given array of lambdas
   for n in range(len(eigvalues)):
       a=np.real(eigvalues[n])**2
       b=np.imag(eigvalues[n])**2
       lambdalength.append(np.sqrt(a+b))
   print(lambdalength)
   return max(lambdalength)

def stabilityFwEuler(maxlambda):
    return 2/maxlambda
#def stabilityRungeKutta(maxlambda):
    return 2.8/maxlambda
#def stabilityModEuler(maxlambda):
    return  (np.sqrt(3)+1)/maxlambda
maxlambdalength = np.round(findmax(eigvalues),10)
print(maxlambdalength)
maxdtFW=stabilityFwEuler(maxlambdalength)
print(maxdtFW)
#maxdtRK=stabilityRungeKutta(maxlambdalength)
#maxdtME=stabilityModEuler(maxlambdalength)
