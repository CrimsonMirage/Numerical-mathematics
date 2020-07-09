"""
Created on Thu Apr 30 15:13:08 2020

@author: Danny
"""

y0 = 1 #start value y0
t0 = 2 #start value t0


def forweuler (t0, y0, tmax, dt):   #Forward Euler
    ts = [t0]
    ws = [y0]
    
    t,w = t0, y0
    while t<tmax:
        tnew=t+dt
        wnew = w+dt*function(t,w)
        t=tnew
        w=wnew
        ts.append(tnew)
        ws.append(wnew)
        print(wnew)
    results = ts, ws
    return results

def function (t,y):
    f= 1+(t-y)**2
    return float(f)
y=forweuler(t0,y0,3,0.5) #numerical results of function y(t), with parameters t0, y0, tmax and delta t

