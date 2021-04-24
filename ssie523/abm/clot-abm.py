import numpy as np
import random
import matplotlib.pyplot as plt
import pycxsimulator as pycx

Dt = 1
n = 1000

class cell:
    pass

def initialize():
    global n, cells, Dt
    cells = []
    for i in range(n):
        c = cell()
        c.x = random.random()
        c.y = random.random() * 0.2
        c.vx = random.random() * 0.03
        c.vy = (random.random() - 0.5) * 0.002
        c.p_stop = 0.00002
        c.p_stick = 0.5
        c.state = 0 
        cells.append(c)
        
def observe():
    global n, cells, Dt
    plt.cla()
    plt.plot([each.x for each in cells if each.state == 0], 
             [each.y for each in cells if each.state == 0], 'bo')
    plt.plot([each.x for each in cells if each.state == 1], 
             [each.y for each in cells if each.state == 1], 'ro')
    plt.axis('image')
    plt.axis([0, 1, -0.2, 0.4])
    plt.show()

  
def update():
    global n, cells, Dt
    for c in cells:
        if c.state == 0:
            # move in (vx, vy)
            c.x += c.vx * Dt
            c.y += c.vy * Dt
            
            if c.x > 1: 
                c.x = 0
            if c.x < 0: 
                c.x = 1
            
            if c.y > 0.2: 
                c.y = 0.2
                c.vy *= -1
            
            if c.y < 0:
                c.y = 0
                c.vy *= -1
            
            if random.random() < c.p_stop:
                c.state = 1
            else:
                for c2 in cells:
                    if c != c2:
                        if c2.state == 1:
                            if (0.5 - abs(c.x - c2.x - 0.5))**2 + (c.y - c2.y)**2 < 0.000005:
                                if random.random() < c.p_stick:
                                    c.state = 1

pycx.GUI().start(func=[initialize, observe, update])