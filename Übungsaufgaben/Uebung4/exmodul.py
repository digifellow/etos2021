import numpy as np
import math
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets

alpha = widgets.FloatSlider(min=0, max=90, step=1, value=30, description=r'$\alpha \, [°]$', continuous_update=False)
ti = widgets.FloatSlider(min=0, max=1.02, step=0.05, value=0.55, description='Zeit [s]', continuous_update=False)


def update_t_range(*args):
    alpha2 =  alpha.value
    v0 = 10      # in m/s
    g = 9.81
    ti.max = 2*v0*math.sin(math.radians(alpha2))/g
alpha.observe(update_t_range, 'value')

def energie_plot(alpha, ti):
    m = 2        # kg
    v0 = 10      # in m/s
    g = 9.81
    tc = 2*v0*math.sin(math.radians(alpha))/g
    t = np.linspace(0, ti, 100)


    vx = v0*math.cos(math.radians(alpha))
    vy = v0*math.sin(math.radians(alpha)) - g*t

    x = (v0*math.cos(math.radians(alpha)))*t
    y = (v0*math.sin(math.radians(alpha)))*t - 0.5*g*t**2

    E_pot = m*y*g
    E_kin = 0.5*m*vy**2 + 0.5*m*vx**2
    E_kin_x = 0.5*m*vx**2

    E_ges = m*y*g + 0.5*m*vy**2 + 0.5*m*vx**2

    fig = plt.figure(figsize=(7.5,10)) 
    ax = fig.add_subplot(3, 1, 1)
    ax.plot(t,y)
    xf = x[len(x)-1]
    yf = y[len(y)-1]
    tf = t[len(t)-1]
    ax.scatter(tf, yf, s=100, color="r")
    ax.set_xlim([0, tc])
    ax.set_title("Ort")
    ax.set_ylabel('y in $m$')
    ax.set_xlabel('Zeit in $s$')
    ax.grid()


    bx = fig.add_subplot(3, 1, 2)
    p1 = bx.plot(t, E_kin)
    p2 = bx.plot(t,E_pot)
    p3 = bx.plot(t, E_ges)
    bx.legend((p1[0], p2[0], p3[0]), ('$E_{kin}$', '$E_{pot}$', '$E_{ges}$'),loc="upper right")
    bx.set_xlim([0, tc])
    bx.set_title("Energieverlauf")
    bx.set_ylabel('Energie in J')
    bx.set_xlabel('Zeit in s')
    bx.grid()

    cx = fig.add_subplot(3, 1, 3)
    e_p = E_pot[len(E_pot)-1]
    e_k = E_kin[len(E_kin)-1]
    e_g = e_k + e_p

    ind = np.arange(4)    # the x locations for the groups
    width = 0.25       # the width of the bars: can also be len(x) sequence

    q1 = plt.bar(ind[0], e_k, width)
    q2 = plt.bar(ind[1], e_p, width)
    q3 = plt.bar(ind[2], e_g, width)
    #q2 = plt.bar(ind[3], E_kin_x, width)
    cx.set_title("Energieerhaltung")
    cx.set_ylabel('Energie in J')
    cx.set_xticks([0,1,2]) 
    cx.set_xticklabels(['$E_{kin}$','$E_{pot}$', '$E_{ges}$'])

    fig.tight_layout()
    return plt.show()