#!/usr/bin/env python
# coding: utf-8
import numpy as np
import math
import matplotlib.pyplot as plt
from ipywidgets import  widgets

def vector_v1(R1, F1):
    mt = 10
    vF = F1*mt
    vR = R1*mt

    xm = 0
    ym = 0

    t = 300/vF
    sD = round(vR*t)

    fig, ax = plt.subplots(figsize=(7.5, 5))
    plt.grid(True)
    ax.set_xlim([-50, 300])
    ax.set_ylim([-50, 350])
    ax.set_xlabel("x-Position [m]")
    ax.set_ylabel("y-Position [m]")
    
    dia = ax.plot([0,sD],[0,300], color='black', linestyle='dashed')

    vR1 = ax.quiver(xm, ym, vR, 0, angles='xy', scale_units='xy', scale=1, color='green')
    vF1 = ax.quiver(xm, ym, 0, vF, angles='xy', scale_units='xy', scale=1, color='green')
    Vg = ax.quiver(xm, ym, vR, vF, angles='xy', scale_units='xy', scale=1, color='red')
    vR_t = plt.text(vR, 0, r'$\vec v_{R}$', fontsize=12)
    vF_t = plt.text(0, vF, r'$\vec v_{F}$', fontsize=12)
    Vg_t = plt.text(vR, vF-15, r'$\vec v_{ges}$', fontsize=12)
    mtb = plt.text(-49, 280, 'Maßstab 10 m:1 m/s', fontsize=12)
    
    v = np.array([[-50,0],[-50,300],[300,300],[300,0]])
    t1 = plt.Polygon(v, color =  'lightblue', alpha = 0.5)
    plt.gca().add_patch(t1)

    return plt.show()

R1 = widgets.FloatSlider(value=7, min=0.001, max=10.5,step=0.5,description=r'$\vec v_{R} \, [m/s]$', style={'description_width': 'initial'}, continuous_update=False)
F1 = widgets.FloatSlider(value=10, min=0.001, max=20.5,step=0.5,description=r'$\vec v_{F} \, [m/s]$', style={'description_width': 'initial'}, continuous_update=False)
#interact(vector_v1, R1 = R1, F1 = F1)

def vector_v2(R2, F2, alpha):
    mt = 10
    vF = F2*mt
    vR = R2*mt
    #alpha = 45

    vFx = -vF*math.sin(math.radians(alpha)) 
    vFy = vF*math.cos(math.radians(alpha))

    xm = 0
    ym = 0
    
    t = 300/vFy
    sD = round((vR+vFx)*t)

    fig, ax = plt.subplots(figsize=(7.5, 5))
    plt.grid(True)
    ax.set_xlim([-200, 300])
    ax.set_ylim([-50, 350])
    ax.set_xlabel("x-Position [m]")
    ax.set_ylabel("y-Position [m]")

    dia = ax.plot([0,0],[0,300], color='gray', linestyle='dashed')
    dia2 = ax.plot([0,sD],[0,300], color='black', linestyle='dashed')
    vR1 = ax.quiver(xm, ym, vR, 0, angles='xy', scale_units='xy', scale=1, color='green')
    vF1 = ax.quiver(xm, ym, vFx, vFy, angles='xy', scale_units='xy', scale=1, color='green')
    Vg = ax.quiver(xm, ym, vR+vFx, vFy, angles='xy', scale_units='xy', scale=1, color='red')
    vR_t = plt.text(vR, 0, r'$\vec v_{R}$', fontsize=12)
    vF_t = plt.text(vFx, vFy, r'$\vec v_{F}$', fontsize=12)
    Vg_t = plt.text(vR+vFx, vFy, r'$\vec v_{ges}$', fontsize=12)
    alpha_t = plt.text(-20, 20, r'$\alpha_F$', fontsize=12)
    mtb = plt.text(-195, 280, 'Maßstab 10 m:1 m/s', fontsize=12)
    v = np.array([[-200,0],[-200,300],[300,300],[300,0]])
    t1 = plt.Polygon(v, color = 'lightblue', alpha = 0.5)
    plt.gca().add_patch(t1)
    
    return plt.show()

R2 = widgets.FloatSlider(value=5, min=0.001, max=10.5,step=0.5,description=r'$\vec v_{R} \, [m/s]$', style={'description_width': 'initial'}, continuous_update=False)
F2 = widgets.FloatSlider(value=9, min=0.001, max=20.5,step=0.5,description=r'$\vec v_{F} \, [m/s]$', style={'description_width': 'initial'}, continuous_update=False)
alpha = widgets.FloatSlider(value=25, min=0, max=90,step=0.5,description=r'$\alpha_R \, [°]$', style={'description_width': 'initial'}, continuous_update=False)

#interact(vector_v2, R2 = R2, F2 = F2, alpha=alpha)

