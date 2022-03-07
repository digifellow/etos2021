#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bokeh.models import Arrow, OpenHead, Text, ColumnDataSource, Label
from bokeh.plotting import figure, show, output_notebook
from bokeh.io import show, push_notebook
from ipywidgets import interact, widgets
import math
# output_notebook() # iirc muss das als output erfolgen, also als letzte zeile einer zelle (?)

#Physik
m = 25
mt = 5/10000
f_l = m*9.81*mt
S = 2000
d = -5*9.81*m/math.sqrt((2*S)**2-(m*9.81)**2)

fx = (math.sqrt(S**2/(1+(d/5)**2)))*mt
fy = fx*d/5

# Arrows
dx = 4.95 
dy = -fy*dx/fx + d

# Plott
p = figure(plot_width=750, plot_height=400, x_axis_label='x-Position [m]',y_axis_label='y-Position [m]',x_range=(-6, 6), y_range=(-0.5, 0.1), title='Aufgabe 1: Kräftediagramm')

# Walls
p.patch(x=[-5.3, -5.3, -5, -5], y=[0.15 , -0.5, -0.5, 0.15], hatch_pattern='right_diagonal_line')
p.patch(x=[5.3, 5.3, 5, 5], y=[0.15 , -0.5, -0.5, 0.15], hatch_pattern='right_diagonal_line')
mytext1 = Label(x=2, y=-0.3, text='Maßstab 1000 kN:5 m')
p.add_layout(mytext1)

# Dicts
cds_arrow_g = ColumnDataSource(dict(xS=[0], yS=[d-f_l+0.001], xE=[0], yE=[d-f_l]))
cds_arrow_mg = ColumnDataSource(dict(xS=[0], yS=[f_l+d-0.001], xE=[0], yE=[f_l+d]))
cds_arrow_s1 = ColumnDataSource(dict(xS=[0], yS=[d], xE=[fx], yE=[-fy+d]))
cds_arrow_s2 = ColumnDataSource(dict(xS=[0], yS=[d], xE=[-fx], yE=[-fy+d]))

cds_lamp = ColumnDataSource(dict(url=['static_ip1/lamp.svg'],x=[-0.39], y=[d], w=[0.79], h=[0.075]))
cds_fg = ColumnDataSource(dict(url=['static_ip1/fg.svg'],x=[0.2], y=[d-f_l], w=[0.35], h=[0.035]))
cds_ffs1 = ColumnDataSource(dict(url=['static_ip1/fs11.svg'],x=[fx-0.2], y=[-fy+d-0.03], w=[0.45], h=[0.035]))
cds_ffs2 = ColumnDataSource(dict(url=['static_ip1/fs2.svg'],x=[-fx], y=[-fy+d-0.03], w=[0.45], h=[0.035]))
cds_fmg = ColumnDataSource(dict(url=['static_ip1/mfg.svg'],x=[0], y=[f_l+d+0.05], w=[0.5], h=[0.04]))

lamp = p.image_url(url='url', x='x', y='y', w='w', h='h', source=cds_lamp)
fg = p.image_url(url='url', x='x', y='y', w='w', h='h', source=cds_fg)
ffs1 = p.image_url(url='url', x='x', y='y', w='w', h='h', source=cds_ffs1)
ffs2 = p.image_url(url='url', x='x', y='y', w='w', h='h', source=cds_ffs2)
fmg = p.image_url(url='url', x='x', y='y', w='w', h='h', source=cds_fmg)

cu1 = p.line([-5,0],[0,d], line_width=1, color = "black") 
cu2 = p.line([5,0],[0,d], line_width=1, color = "black") 
dia = p.line([-fx,fx],[-fy+d,-fy+d], line_width=1, line_dash="dashed") 

#Gewicht
g = p.line([0,0],[d,d-f_l], color = "firebrick", line_width=4)
g_a = p.add_layout(Arrow(end=OpenHead(line_color="firebrick", line_width=4),
                    x_start='xS', y_start='yS', x_end='xE', y_end='yE', source=cds_arrow_g))

#S1
s1 = p.line([0,fx],[d,-fy+d], color = "green", line_width=4)
s1_a = p.add_layout(Arrow(end=OpenHead(line_color="green", line_width=4),
                    x_start='xS', y_start='yS', x_end='xE', y_end='yE', source=cds_arrow_s1))

#S2
s2 = p.line([0,-fx],[d,-fy+d], color = "green", line_width=4)
s2_a = p.add_layout(Arrow(end=OpenHead(line_color="green", line_width=4),
                    x_start='xS', y_start='yS', x_end='xE', y_end='yE', source=cds_arrow_s2))

#Parallelogramm
mg = p.line([0,0],[d,f_l+d], color = "green", line_width=4)
mg_a = p.add_layout(Arrow(end=OpenHead(line_color="green", line_width=4),
                    x_start='xS', y_start='yS', x_end='xE', y_end='yE', source=cds_arrow_mg))

p1 = p.line([fx,0],[-fy+d,f_l+d], color = "green", line_width=4, line_dash="dashed")
p2 = p.line([-fx,0],[-fy+d,f_l+d], color = "green", line_width=4, line_dash="dashed")

def vector_plot(b):
    m = 25
    S = b*10**3
    f_l = m*9.81*mt
    d = -5*9.81*m/math.sqrt((2*S)**2-(m*9.81)**2)
    fx = (math.sqrt(S**2/(1+(d/5)**2)))*mt
    fy = fx*d/5
    dy = -fy*dx/fx + d
    # lines  
    g.data_source.data['y'] = [d,d-f_l]
    s1.data_source.data['x'] = [0,fx]
    s1.data_source.data['y'] = [d,-fy+d]
    s2.data_source.data['x'] = [0,-fx]
    s2.data_source.data['y'] = [d,-fy+d]
    mg.data_source.data['y'] = [d,f_l+d] 
    p1.data_source.data['x'] = [fx,0]
    p1.data_source.data['y'] = [-fy+d,f_l+d]
    p2.data_source.data['x'] = [-fx,0]
    p2.data_source.data['y'] = [-fy+d,f_l+d]
    cu1.data_source.data['y'] = [0,d]
    cu2.data_source.data['y'] = [0,d]
    dia.data_source.data['x'] = [-fx,fx]
    dia.data_source.data['y'] = [-fy+d,-fy+d]
    # figures  
    lamp.data_source.data['y'] = [d]
    fg.data_source.data['y'] = [d-f_l]
    ffs1.data_source.data['x'] = [fx-0.2]
    ffs1.data_source.data['y'] = [-fy+d-0.03]
    ffs2.data_source.data['x'] = [-fx]
    ffs2.data_source.data['y'] = [-fy+d-0.03]
    fmg.data_source.data['y'] = [f_l+d+0.05]
    # arrows
    cds_arrow_g.stream(dict(xS=[0], yS=[d-f_l+0.001], xE=[0], yE=[d-f_l]),rollover=1)
    cds_arrow_mg.stream(dict(xS=[0], yS=[f_l+d-0.001], xE=[0], yE=[f_l+d]),rollover=1)
    cds_arrow_s1.stream(dict(xS=[0], yS=[d], xE=[fx], yE=[-fy+d]),rollover=1)
    cds_arrow_s2.stream(dict(xS=[0], yS=[d], xE=[-fx], yE=[-fy+d]),rollover=1)
    push_notebook()

belastung = widgets.FloatSlider(value=7, min=2, max=9,step=0.5,description='max. Belastung [kN]', style={'description_width': 'initial'})
returnvalue=show(p, notebook_handle=True)
#interact(vector_plot, b = belastung)


# In[ ]:




