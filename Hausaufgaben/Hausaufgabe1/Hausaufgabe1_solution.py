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
# ## Hausaufgabe 1: Physikalische Größen und Einheiten
# 
# 

# <div style= "color: black;background-color: rgba(0,177,172, 0.1) ;margin: 10 px auto; padding: 10px; border-radius: 10px">
# <p style="font-size:12pt; text-align:center; color: black;background-color: rgba(0,177,172, 0.1) ;margin: 10 px auto; padding: 10px; border-radius: 10px" id="2"><b>  Hausaufgabe - Stau</b>  </p> 
# In einem langen Stau stehen $750$ Autos, die sehr langsam mit Schrittgeschwindigkeit ($5~\text{km/h}$) direkt hintereinander fahren. Jedes Auto benötigt eine Länge von durchschnittlich $5,4~\text{m}$. 
#     

# <font style="background-color:#BFBFBF "> **Vorgehensweise  :**</font>
# 
# 1. Wie lang ist der Stau in Kilometer?

# In[2]:


anzahl = 750    # Anzahl der Autos
l_auto = 5.4    # Länge des Autis im m

l_stau = anzahl*l_auto*1/1000 # Stau in km

print("Der Stau ist %.2f km lang." % l_stau)


# 2. Wie viele Autos durchfahren den Stau in einer Stunde?

# In[4]:


strecke = 5*1000/1  # zurückgelegte Strecke in einer Stunde in m

d_autos = strecke/l_auto 

print("%.0f Autos durchfahren den Stau in einer Stunde." % d_autos)


# 3. Ein Auto verbraucht 8,2 Liter Benzin pro 100 Kilometer. Wie viel verbraucht ein Auto in Kubikzentimeter pro Meter?

# In[6]:


verbrauch_1 = 8.2/100  # Verbrauch in L/km

UF1 = 1000/1    # 1 L entspricht 1000 cm³
UF2 = 1/1000    # 1 km entspricht 1000 m

verbrauch_2 = verbrauch_1*UF1*UF2 # Verbrauch in cm³/m

print("Ein Auto verbraucht %.3f cm³/m." % verbrauch_2)


# 4. Wie viele Liter Benzin verbraucht ein Auto, um einmal die Erde zu umrunden (Erdumfang ca. $40.000~\text{km}$)?

# In[8]:


erd_umf = 40000   # Erdumfang im km

verbrauch = verbrauch_1*erd_umf #Verbrauch in Litern

print("Das Auto verbraucht %.0f Liter Benzin." % verbrauch)


# 5. Wiederholen Sie die Ausgabe von Aufgabeteil 4, nun aber mit drei signifikanten Stellen in Exponentialschreibweise.

# In[10]:


print("Das Auto verbraucht %1.2e Liter Benzin." % verbrauch)

