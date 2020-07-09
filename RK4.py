# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:39:22 2020

@author: Danny
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def truncationError( wnum, wnum2,dt):
    #determine trucation error
    t = 1/dt #time for error at certain point in time
    errors = wnum[:,-1] - wnum2[:,-1]
    p = 4
    print('\nThe errors are ',errors[0],' for y1 and ',errors[1],' for y2 at time t=', t)
    cp=errors/((dt**p)*((2**p)-1)) #cp is calculated according to formula 6.46 in the book Numerical methods for ordinary differential equations
    #print(cp)
    truncer = cp*(dt**p) #truncaton error
    print('\n The truncation error is: ', truncer)
    #diff = cp*(dt**p)*((2**p)-1)
    #print(diff)

def RungeKutta4step(tn, wn, dt, f):
    #A single step of RungeKutta method
    k1 = dt * f(tn,wn)
    k2 = dt * f(tn+(dt/2), wn+(k1/2))
    k3 = dt * f(tn+(dt/2), wn+(k2/2))
    k4 = dt * f(tn+dt, wn+k3)
    
    wnplus1 = wn + (k1+2*k2+2*k3+k4)/6
    return wnplus1

def W(t,W0):
    #The recursive formula for determining W0 over the time
    if 0 <= t < 3/12 or 8/12 < t < 1: 
        wt=0
    elif  3/12 <= t <= 8/12:
        wt= W0
    elif t >= 1:
        wt=W(t-1,W0)
    return wt

def righthandsidefunction(t,y):
    #variables
    a=2
    c=3.92
    alpha=2*(10**-3)
    gamma = 7*(10**-3)
    global w0 #global W0 is used for the automated check for which W0 is allowed
    y1=y[0]
    y2=y[1]
    
    #System of equation given in the problem
    f1=(a-alpha*y2)*y1-W(t,w0)*y1
    f2=(gamma*y1-c)*y2
    
    return np.array([f1,f2])
    
def RungeKutta4method(t0, tmax, dt, f, y0):
    #The RungeKutta method from begin point t0 until end point tmax, with a given timestep dt, for a function f with start values y0 
    N= int(np.round((tmax-t0)/dt)) #calculation of the amount of steps necessary
    time = np.linspace(t0, tmax, N+1) #let's make every step a nice equal distance away from the other
    dt= (tmax-t0)/N #Should be equal to dt if N is correct
    
    w = np.zeros((y0.size,N+1)) #a nice empty array for our beloved population values
    w[:,0] = y0
    for n,tn in enumerate(time[:-1]):
        w[:,n+1] = RungeKutta4step(tn,w[:,n],dt,righthandsidefunction)
        if (w[1,n+1] <= 250.0000 ):
            print('y2 is smaller than 200 at timestep: ',n+1,' with y1 = ', w[1,n+1])
    return time, w

# Set all known values and settings
w0=1.882
t0 = 0
tmax = 10
y0 = np.array([600,1000])
dt = 0.5/(2**7)
minval=[]
# Execute the method
while True:
    print('checking for w0= ', np.round(w0,7))
    tnum, wnum = RungeKutta4method(t0,tmax,dt,righthandsidefunction,y0)
    miny2=min(wnum[1,:])
    minval.append((w0,miny2))
    if min(wnum[1,:])<= 250:
        w0=np.round(w0,6)
        print('y2 got smaller than 250 with w0 = ', w0)
        break
    w0=w0+0.00008 
table2 = pd.DataFrame(minval, columns=['w0','minval']).transpose()
#table2.plot(kind='line', x='w0', y= 'minval')
plt.show()
tnum2, wnum2 = RungeKutta4method(t0,tmax,2*dt,righthandsidefunction,y0)
truncationError(wnum, wnum2, dt)

    # Make a nice table
alldata = np.concatenate(([tnum],wnum),axis=0).transpose()
table = pd.DataFrame(alldata,columns=['t','y1(t)','y2(t)'])
print('\nA nice table of the simulation:\n')
print(table)
    
    # Make a nice picture
plt.close('all')
plt.figure()
plt.plot(tnum,wnum[0,:],label='$y_1$',marker='o',linestyle='-')
plt.plot(tnum,wnum[1,:],label='$y_2$',marker='o',linestyle='-')
plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.title('Simulation')
plt.legend()
