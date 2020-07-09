# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:16:44 2020

@author: Danny
"""

import numpy as np
def g(t):
    return [0.,10.*t]

y0 = np.array([4,5])
sys =[[3.,1.],[2., 0.]]
dt = 0.1
t0 = 0
tmax = 2

def ModEulerStep(tn,wn, dt):
    wbar = wn + dt*(np.dot(sys, wn) + g(tn))
    print(wbar)
    wnew = wn + (dt/2)*((np.dot(sys,wbar)+g(tn+dt)) + (np.dot(sys, wn)))
    return wnew
def ModEuler(t0, tmax, dt,sys, y0):
    N = int(np.round((tmax-t0)/dt)) 
    time = np.linspace(t0, tmax, N+1)
    dt = (tmax-t0)/N
    w = np.zeros((y0.size,N+1))
    w[:,0] = y0
    for n,tn in enumerate(time[:-1]):
        w[:,n+1] = ModEulerStep(tn,w[:,n],dt)
    return time, w
tnum, wnum = ModEuler(t0,tmax,dt,sys,y0)