import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from ipywidgets import interact, FloatSlider

A1 = 0.8 # anfahrts-beschl
A3 = -1.2 # brems-beschl.

@np.vectorize # allows to use arrays for t
def get_avx(t, T1, T2, T3):
    """
    Berechnet Position etc. der S-Bahn abhängig von den End-Zeiten der drei Phasen
    Arguments: T1, T2, T3 (number) , t (number or after vectorization an array)
    Returns: a,v,x (number)
    """
    if t < T1:
        a = A1
        v = A1 * t
        x = 0.5 * A1 * t**2
    elif t < T2:
        a = 0.0
        v = A1 * T1
        x = 0.5 * A1 * T1**2 + (A1 * T1) * (t-T1)
    elif t < T3:
        a = A3
        v = A1 * T1 + A3 * (t-T2)
        x = 0.5 * A1 * T1**2 + (A1 * T1) * (t-T1) + 0.5 * A3 * (t-T2)**2
    else:
        return None, None, None
    return a,v,x

def plot_empty_txva(rangeT=[0,100], rangeX=[0,1100], rangeV=[-10,50], rangeA=[-1.5,1.5], N=301):
    """
    Create empty plots for t-x, t-v, t-a Diagrams.
    Returns: fig, lineX, lineV, lineA: handles to parts of diagram
    Returns: t: shape (N,)
    """
    
    fig, (axX, axV, axA) = plt.subplots(3, 1, sharex=True)
    #fig.subplots_adjust(hspace=0)
    
    t = np.linspace(rangeT[0], rangeT[1], N)
    a = np.linspace(rangeA[0], rangeA[1], N)
    v = np.linspace(rangeV[0], rangeV[1], N)
    x = np.linspace(rangeX[0], rangeX[1], N)
    
    lineX, = axX.plot(t, x, 'r')
    lineV, = axV.plot(t, v, 'g')
    lineA, = axA.plot(t, a, 'b')

    axA.set(xlabel="$t$ [s]")
    
    fig.align_ylabels()
    axX.set_ylabel("$x$ [m]")
    axV.set_ylabel("$v$ [m/s]")
    axA.set_ylabel("$a$ [m/s²]")
    
    axX.hlines(y=1000.0, xmin=rangeT[0], xmax=rangeT[1], linestyles='--', colors='grey')
    axV.hlines(y=0.0, xmin=rangeT[0], xmax=rangeT[1], linestyles='--', colors='grey')
    axV.hlines(y=15.0, xmin=rangeT[0], xmax=rangeT[1], linestyles='--', colors='lightgrey')
    
    axA.set_yticks([A1,0.0,A3])

    return fig, lineX, lineV, lineA, t

def update(T1,T2,T3, ctx):
    """
    Update the empty plot with actual data.
    """
    fig, lineX, lineV, lineA, t_array = ctx
    
    a,v,x = get_avx(t_array, T1, T1+T2, T1+T2+T3)
    lineX.set_ydata(x)
    lineV.set_ydata(v)
    lineA.set_ydata(a)

def update_display(ctx):
    fig, lineX, lineV, lineA, t_array = ctx

    fig.canvas.draw_idle()

def redraw(T1,T2,T3):
    ctx = plot_empty_txva()
    update(T1,T2,T3, ctx)
    plt.show()
    
def display_plot(widget=True):
    T1_slider = FloatSlider(description="$t_1$", value=10.0, min=0.0, max=100, continuous_update=False)
    T2_slider = FloatSlider(description="$t_2$",value=20.0, min=0.0, max=100, continuous_update=False)
    T3_slider = FloatSlider(description="$t_3$",value=30.0, min=0.0, max=100, continuous_update=False)
    
    if widget:
        ctx = plot_empty_txva()
    
        def upd(T1,T2,T3):
            update(T1,T2,T3,ctx)
        interact(upd, T1=T1_slider,T2=T2_slider,T3=T3_slider);
    else:
        interact(redraw, T1=T1_slider,T2=T2_slider,T3=T3_slider);