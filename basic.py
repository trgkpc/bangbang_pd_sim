#!/usr/bin/python3.6
import matplotlib.pyplot as plt

def simulator(x0, v0, controller, plot=True):
    dt = 0.001
    tmax = 10.0
    
    x = x0
    v = v0
    t = 0.0
    
    history = [[],[],[]]
    while t <= tmax:
        a = controller(x, v)
        x += v * dt + 0.5 * a * (dt**2)
        v += a * dt
        t += dt

        hoge = [history[i].append([t,x,v][i]) for i in [0,1,2]]

    if plot:
        plt.plot(history[0], history[1])
        plt.show()
    return history
