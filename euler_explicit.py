# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:19:09 2021

@author: auro005
"""
### Euler Explicit ODE solver

from math import *
import numpy as np
from matplotlib.pylab import *
def f(x):
    return(-10.0*x)
d_t = 10**-2
n = 10**3
y=[]
y.append(1.0)
t=[]
t.append(0.0)
y_exact=[]
y_exact.append(1.0)
for i in range(1,n,1):
    y.append(y[i-1] + d_t*(f(y[i-1])))
    t.append(t[i-1]+d_t)
    y_exact.append(e**(-10*t[i]))
plot(t,y)
plot(t,y_exact)
show()
    