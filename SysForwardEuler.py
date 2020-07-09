# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:45:35 2020

@author: Danny
"""
import numpy as np
def g(t):
    return [0.,10.*t]

y0 = np.array([1,5])
sys =[[3.,1.],[2., 0.]]
dt = 0.1
t0 = 0
tmax = 5

def ForwardEulerStep(tn,wn, dt):
    wnew = wn + dt*(np.dot(sys, wn) + g(tn))
    return wnew
def ForwardEuler(t0, tmax, dt,sys, y0):
    N = int(np.round((tmax-t0)/dt)) #calculation of the amount of steps necessary
    time = np.linspace(t0, tmax, N+1) #let's make every step a nice equal distance away from the other
    dt = (tmax-t0)/N #Should be equal to dt if N is correct
    w = np.zeros((y0.size,N+1))
    w[:,0] = y0
    for n,tn in enumerate(time[:-1]):
        w[:,n+1] = ForwardEulerStep(tn,w[:,n],dt)
    return time, w
tnum, wnum = ForwardEuler(t0,tmax,dt,sys,y0)