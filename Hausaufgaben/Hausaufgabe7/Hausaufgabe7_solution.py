#!/usr/bin/env python
# coding: utf-8

# <div>
#     <img src="static/FHAachen-logo2.svg" style="float: right;height: 15em;">
# </div>
# <div>
#     <img src="static/IIIPIB_RWTH.png" style="float: right;height: 6.5em;">
# </div>
# 
# **Einführung in die Physik im SS 2021** \
# **Darius Mottaghy**        \
# **Stefan Roth**
# 
# ## Hausaufgabe 7: Thermodynamische Prozesse
# 
# 

# <div style= "color: black;background-color: rgba(0,177,172, 0.1) ;margin: 10 px auto; padding: 10px; border-radius: 10px">
# <p style="font-size:12pt; text-align:center; color:   black;background-color: rgba(0,177,172, 0.1) ;margin: 10 px auto; padding: 10px; border-radius: 10px" id="3"><b>  Aufgabe - isobare Zustandsänderung </b>  </p> 
#     
# Bei einer isobaren Expansion ändert sich der Druck nicht. Zeichnen Sie verschiedene Isobaren für ein ideales Gas, die das Volumen als Funktion der Temperatur darstellen. <br>
# 
# </div>  
# 
# 
# <font style="background-color:#BFBFBF "> **Hinweise :**</font> <br>
# 
# 1. Leiten Sie aus der idealen Gasgleichung eine Formel für das Volumen her.

# **Lösung**     
# 
# Aus der idealen Gasgleichung mit $n, R$ und $p$ konst. wird $V(T)$ hergeleitet:
# 
# $$V(T) = \frac{nR}{p}T$$

# 2. Implementieren Sie das Volumen als eine Funktion von dem Druck und der Temperatur.

# In[2]:


import numpy as np

n = 1        # mol
R = 8.314    # in K⁻¹⋅mol⁻¹ 

def V(T,p):
    return n*R*T/p


# 3. Plotten Sie für verschiedene Drücke das Volumen über der Temperatur zwischen $273,15~\mathrm{K}$ und $373,15~\mathrm{K}$. Bspw. für $250, 500$ und $750~\mathrm{Pa}$. Beachten Sie, dass die Temperatur in Kelvin übergeben werden sollte.

# In[4]:


import matplotlib.pyplot as plt

T = np.linspace(273.15,373.15)

fig = plt.figure(figsize=(7.5,5))
plt.plot(T, V(T,750),label='$p=750$ Pa')
plt.plot(T, V(T,500),label='$p=500$ Pa')
plt.plot(T, V(T,250),label='$p=250$ Pa')
plt.xlabel("T in K")
plt.ylabel("V in m³")   
plt.legend(loc="upper left")

