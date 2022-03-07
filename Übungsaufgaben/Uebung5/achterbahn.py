import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
from matplotlib.widgets import Button
import math
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim([0, 62])
ax.set_ylim([0, 35])
ax.set_xlabel("x-Position [m]")
ax.set_ylabel("y-Position [m]")
#plt.xticks([])
fmes = []
str1 = 'static/frames/00'
for i in range(0,38):
    str2 = str(2*i+1) + '.png'
    p = str1 + str2
    img = mpimg.imread(p)
    fmes.append([plt.imshow(img, extent=[0, 62, 0, 35], animated=True)])

ani = animation.ArtistAnimation(fig, fmes, interval=750,repeat_delay=60)

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
x = []
y = []
t = []
phi = []
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    
    if ix > 1:
        x.append((round(ix,2)))
        y.append((round(iy,2)))
        fr = ani._framedata.index(next(ani.frame_seq)) - 1
        t.append(round(2.10/38*fr,3))
        phi_i = math.atan((iy-19.46)/(ix-34))
        if phi_i < 0:
            phi.append((round((math.pi+phi_i),3)))
        else:
            phi.append((round((phi_i),3)))
            
    if len(x) == 100:
        fig.canvas.mpl_disconnect(cid)

    return t, x, y, phi
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()