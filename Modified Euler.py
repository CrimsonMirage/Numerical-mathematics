# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:38:14 2020

@author: Danny
"""


y0 = 1 #start value y0
t0 = 2 #start value t0


def modeuler (t0, y0, tmax, dt):    #ModifiedEuler
    ts = [t0]
    ws = [y0]
    
    t,w = t0, y0
    while t<tmax:
        tnew=t+dt
        waux = w+dt*function(t,w)
        wnew = w+dt/2*(function(t,w)+function(tnew,waux))
        t=tnew
        w=wnew
        ts.append(tnew)
        ws.append(wnew)
        print(wnew)
    results = ts, ws
    return results

def function (t,y): #function from the differential equation
    f= 1+(t-y)**2
    return float(f)
y=modeuler(t0,y0,3,0.5) #numerical results of function y(t), with parameters t0, y0, tmax and delta t

