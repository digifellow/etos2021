#!/usr/bin/env python
# coding: utf-8

import numpy as np
import math
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets

def reibung_plots(**kwargs):
    """
    Return forces vs. parameter diagramm depending of the given parameters. Possible combinations:
    1. Force vs. Mass: give your calculated F_R, F_H and the mass m which you used for it.
    2. Force vs. Coefficient of static friction: give your calculated F_R, F_H and the coefficient of static friction mu_H which you used for it.
    3. Force vs. Angle: give your calculated F_R, F_H and the angle alpha which you used for it.
    4. Forces vs. Angle for 3 different masses: give alpha and three different masses.
    
    Parameters
    ----------
    F_R: float or ndarray
        friction force
    F_H: float or ndarray
        slope downforce       
    m : float or ndarray
        mass of object
    alpha: float or ndarray
        inclination
    mu_H: float or ndarray
        coefficient of static friction

    Returns
    -------
    matplotlib.object
        Matplotlib plot
    """

    if not kwargs:
        print("Arguments are empty")
    else:
        given_arguments = [*kwargs]
        comparation_string = ['F_R', 'F_H', 'm', 'alpha', 'mu_H']
        
    if 'F_R' in given_arguments and 'F_H' in given_arguments and 'm' in given_arguments:
        try:
            plt.plot(kwargs['m'], kwargs['F_R'], 'r', label='$F_R$') 
            plt.plot(kwargs['m'], kwargs['F_H'], 'g', label='$F_H$')
            plt.xlabel('Masse [kg]')
            plt.ylabel('Kraft [N]')
            plt.legend(loc="upper left")
            plt.show()
        except:
            print("The arguments must have the same dimension") 
    
    
    elif 'F_R' in given_arguments and 'F_H' in given_arguments and 'mu_H' in given_arguments and 'alpha' not in given_arguments:
        try:
            plt.plot(kwargs['mu_H'], kwargs['F_R'], 'r', label='$F_R$')
            plt.plot(kwargs['mu_H'], kwargs['F_H'], 'g', label='$F_H$')
            plt.xlabel('Haftreibungskoeffizient')
            plt.ylabel('Kraft [N]')
            plt.legend(loc="upper left")
            plt.show()
        except:
            print("The arguments must have the same dimension") 
    
    elif 'F_R' in given_arguments and 'F_H' in given_arguments and 'alpha' in given_arguments and 'mu_H' not in given_arguments:
        try:
            plt.plot(kwargs['alpha'], kwargs['F_R'], 'r') 
            plt.plot(kwargs['alpha'], kwargs['F_H'], 'g')
            plt.xlabel('Neigungswinkel [°]')
            plt.ylabel('Kraft [N]')
            plt.legend(loc="upper left")
            plt.show()
        except:
            print("The arguments must have the same dimension") 
        
    elif 'alpha' in given_arguments and 'mu_H' in given_arguments:
        
        try:
            F_R = kwargs['F_R']
            F_H = kwargs['F_H']
            F_R = np.vectorize(F_R)
            F_H = np.vectorize(F_H)
            fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))
            fig.suptitle('Kräfte bei 80kg, 100kg und 120 kg ')
            ax1.set_ylabel('Kraft [N]')
            ax1.set_xlabel('Neigung [°]')
 
            ax1.plot(kwargs['alpha'], F_R(kwargs['alpha'], 80, kwargs['mu_H']), label='$F_R$', color='red')
            
            ax1.plot(kwargs['alpha'], F_H(kwargs['alpha'], 80, kwargs['mu_H']), label='$F_H$', color='green')
        
            ax1.set_ylim([0, 1200])
            ax1.legend(loc="upper left")
    
            ax2.plot(kwargs['alpha'], F_R(kwargs['alpha'], 100, kwargs['mu_H']), label='$F_R$', color='red')
            ax2.plot(kwargs['alpha'], F_H(kwargs['alpha'], 100, kwargs['mu_H']), label='$F_H$', color='green')
            ax2.set_ylim([0, 1200])
            ax2.legend(loc="upper left")
            ax2.set_xlabel('Neigung [°]')

            ax3.plot(kwargs['alpha'], F_R(kwargs['alpha'], 120, kwargs['mu_H']), label='$F_R$', color='red')
            ax3.plot(kwargs['alpha'], F_H(kwargs['alpha'], 120, kwargs['mu_H']), label='$F_H$', color='green')
            ax3.set_ylim([0, 1200])
            ax3.legend(loc="upper left")
            ax3.set_xlabel('Neigung [°]')
        except:
            print("Error reading F_H or F_R") 
    
    else:
        print("No combination available")   

dr = widgets.FloatSlider(min=0.07, max=0.30, step=0.01, value=0.09, description='d [m]', continuous_update=False)
b = widgets.FloatSlider(min=2, max=9.0, step=0.5, value=7.0, description='Seilkraft [kN]', continuous_update=False)

def update_dr(*args):
    S = b.value*10**3
    d = 5*9.81*25/math.sqrt((2*S)**2-(25*9.81)**2)
    dr.value = d
b.observe(update_dr, 'value')

def update_b(*args):
    d =  dr.value
    S = 1/2*math.sqrt(((5*25*9.81)/d)**2+(25*9.81)**2)
    b.value = S/(10**3)
dr.observe(update_b, 'value')
        
def vector_plot1(b, dr):
    m = 25
    mt = 5/10000
    f_l = m*9.81*mt
    S = b*10**3
    d = 5*9.81*m/math.sqrt((2*S)**2-(m*9.81)**2)
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.grid(True)
    ax.set_xlim([-5, 5])
    ax.set_ylim([-0.5, 0.1])
    ax.set_xlabel("x-Position [m]")
    ax.set_ylabel("y-Position [m]")
    fx = (math.sqrt(S**2/(1+(d/5)**2)))*mt
    fy = -fx*d/5
    l1 = ax.plot([-5,0],[0,-d], color='black')
    l2 = ax.plot([5,0],[0,-d], color='black')
    l3 = ax.plot([-fx,0],[-fy-d,-d+f_l], color='green')
    l4 = ax.plot([fx,0],[-fy-d,-d+f_l], color='green')
    dia = ax.plot([-fx,fx],[-fy-d,-fy-d], color='green', linestyle='dashed')
    s1 = ax.quiver(0, -d, fx, -fy, angles='xy', scale_units='xy', scale=1, color='green')
    s2 = ax.quiver(0, -d, -fx, -fy, angles='xy', scale_units='xy', scale=1, color='green')
    g = ax.quiver(0, -d, 0, -f_l, angles='xy', scale_units='xy', scale=1, color='red')
    mg = ax.quiver(0, -d, 0, f_l, angles='xy', scale_units='xy', scale=1, color='green')
    s1_t = plt.text(fx, -d, r'$\vec F_{S_{1}}$', fontsize=12)
    s2_t = plt.text(-fx, -d, r'$\vec F_{S_{2}}$', fontsize=12)
    g_t = plt.text(0, -d-f_l-0.04, r'$\vec F_{G}$', fontsize=12)
    mg_t = plt.text(0, f_l-d, r'$-\vec F_{G}$', fontsize=12)
    mt = plt.text(-4.5, -0.45, 'Maßstab 2 kN:1 m', fontsize=12)
    return plt.show()

#b = widgets.FloatSlider(value=7, min=2, max=9,step=0.5,description='Seilkraft [kN]', style={'description_width': 'initial'})
#interact(vector_plot1, b = b)

def vector_plot2(n):
    # Physik
    mt = 50/422000 #Maßstab
    F_S = 422000
    F_S = F_S*mt
    L = 315
    #n = 0.2

    alpha = math.atan(n)
    s = math.sin(alpha)
    c = math.cos(alpha)

    F_G = F_S/s
    F_H = F_G*s
    F_N = F_G*c

    x_i = 0
    x_f = 315

    #mittel
    x_m = x_f/2*c 
    y_m = x_f/2*s
    
    x_fr = x_f*c 
    y_fr = x_f*s

    #F_S
    fsx = F_S
    fsy = 0

    fsxr = fsx*c + x_m
    fsyr = fsx*s + y_m

    #F_G
    fgy = y_m - F_G

    #F_H
    fhxr = x_m - F_H*c
    fhyr = y_m - F_H*s
    #F_N
    fnx = 0
    fny = F_N

    fnxr = fny*s + x_m
    fnyr = y_m - fny*c

    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    plt.grid(True)
    ax.set_xlim([0, 350])
    ax.set_ylim([-250,150])
    ax.set_xlabel("x-Position [m]")
    ax.set_ylabel("y-Position [m]")
    #ax.set_ylabel(r'$y-Position$')
    g = ax.quiver(x_m, y_m, 0, -F_G, scale_units='xy', scale=1, color='green')
    f_h = ax.quiver(x_m, y_m, -F_H*c, -F_H*s+2, scale_units='xy', scale=1, color='blue')
    f_n = ax.quiver(x_m, y_m, fny*s, -fny*c, scale_units='xy', scale=1, color='blue')
    f_s = ax.quiver(x_m, y_m, fsx*c, fsx*s-2, scale_units='xy', scale=1, color='red')
    mt = plt.text(5, -225, 'Maßstab 422 kN:50 m', fontsize=12)
    g_t = plt.text(x_m, fgy-10, r'$\vec F_{G}$', fontsize=12)
    fh_t = plt.text(fhxr-20, fhyr, r'$\vec F_{H,G}$', fontsize=12)
    fn_t = plt.text(fnxr, fnyr, r'$\vec F_{N,G}$', fontsize=12)
    fs_t = plt.text(fsxr, fsyr, r'$\vec F_{S}$', fontsize=12)   
    v = np.array([[0,0], [x_fr,y_fr], [x_fr,0]])

    t1 = plt.Polygon(v, color='blue', alpha=0.3)
    plt.gca().add_patch(t1)
    
    return plt.show()

n = widgets.FloatSlider(value=0.3, min=0.2, max=0.5,step=0.05,description='Steigung')
#interact(vector_plot2, n = n)

