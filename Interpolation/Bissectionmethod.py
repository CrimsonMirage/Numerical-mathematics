import math as math
import numpy as np

borderl = -2 #left interval
borderr = 1.5 # right interval
length = 0 #requested pn --> aka n'th interation, otherwise we just calculate a very big iteration
tolerance = math.sqrt(np.finfo(float).eps)
maxIt = 10000 if length == 0 else length
pn = [0]*(maxIt)

def functionval(x):
    f = 3*(x+1)*(x-0.5)*(x-1)
    return f

def bissection(borderl, borderr, length=maxIt, tol=tolerance):
    for j in range(length):     
        pn[j] = (borderl+borderr)/2
        if (functionval(borderl)*functionval(pn[j])<0):
            borderr=pn[j]
        else:
            borderl=pn[j]
        iterationindex=j
        conv = (abs(pn[j]-pn[j-1]))/abs(pn[j])
        print(conv)
        if conv<tol:
            return pn[iterationindex],iterationindex
    return pn[iterationindex],iterationindex

pval = bissection(borderl, borderr, maxIt)
print('p(',pval[1],') is: ',pval[0])
