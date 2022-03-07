#!/usr/bin/env python
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
from matplotlib.widgets import Button

fig, ax = plt.subplots(figsize=(7.5, 6))
ax.set_xlim([0, 225])
ax.set_ylim([380, 0])
#ax.set_xlabel("x-Position [cm]")
ax.set_ylabel("y-Position [cm]")
plt.xticks([])
fmes = []
str1 = 'static/frames/02'
j=28
for i in range(0,27):
    str2 = str(j) + '.png'
    p = str1 + str2
    img = mpimg.imread(p)
    fmes.append([plt.imshow(img, extent=[0, 225, 380, 0], animated=True)])
    j = j + 1

ani = animation.ArtistAnimation(fig, fmes, interval=500,repeat_delay=60)

# From matplotlib: https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/animation.py, edited
def start(event):
    """
    Starts interactive animation. Adds the draw frame command to the GUI
    hanler, calls show to start the event loop.
    """
        
    # First disconnect our draw event handler
    ani._fig.canvas.mpl_disconnect(ani._first_draw_id)
    # Now do any initial draw
    ani._init_draw()

    # Add our callback for stepping the animation and
    # actually start the event_source.
    ani.event_source.add_callback(ani._step)
    ani.event_source.start()

def stop(event):
    # On stop we disconnect all of our events.
        
    ani._fig.canvas.mpl_disconnect(ani._close_id)
    ani.event_source.remove_callback(ani._step)

axpause = plt.axes([0.75, 0.05, 0.1, 0.075])
axstart = plt.axes([0.85, 0.05, 0.1, 0.075])
pause_button = Button(axpause, 'Pause')
pause_button.on_clicked(stop)
start_button = Button(axstart, 'Start')
start_button.on_clicked(start)

# From https://stackoverflow.com/questions/25521120/store-mouse-click-event-coordinates-with-matplotlib, edited
s = []
t = []
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    
    if ix > 1:
        s.append((round(iy/100,2)))
        fr = ani._framedata.index(next(ani.frame_seq)) - 1
        t.append(round(1/30*fr,3))

    if len(s) == 27:
        fig.canvas.mpl_disconnect(cid)

    return y_koordinaten
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()