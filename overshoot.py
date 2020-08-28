#!/usr/bin/python3.6
import matplotlib.pyplot as plt
from basic import simulator
from math import exp

def gain(time_const):
    Kp = 1/(time_const**2)
    Kd = 2/(time_const)
    return [Kp, Kd]

def overshoot(x0, v0, time_const):
    m = min(x0, 0)
    Kp, Kd = gain(time_const)
    k = 0.5 * Kd
    A = x0
    B = v0 + k*x0
    if B!=0 and k!=0:
        t = v0 / (B*k)
        if t > 0:
            x = A * exp(-k*t) + B*t*exp(-k*t)
            m = min(x, m)
    return m

def pd(x, v, umax):
    tconst = 1.0
    Kp, Kd = gain(tconst)
    u = -Kp*x - Kd*v
    if u > umax:
        return umax
    elif u < -umax:
        return -umax
    return u

init = [2.0, -2.0]
t0,x0,v0 = simulator(init[0], init[1], lambda x,v:pd(x,v,10.0), plot=False)
t1,x1,v1 = simulator(init[0], init[1], lambda x,v:pd(x,v,1.0), plot=False)

plt.plot(t0, x0, label="acc no-limit")
plt.plot(t1, x1, label="acc limited")
plt.legend()
plt.grid()
plt.show()

