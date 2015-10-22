#William Mackay
#MTH 337 Report 06 Python Script- Planet orbiting a binary star system

from pylab import *
from matplotlib import animation

#Defining Functions to simulate orbits
def sun_position(R,t):
    x1=R*cos(t)
    x2=-x1
    y1=R*sin(t)
    y2=-y1
    return x1,x2,y1,y2

def diff_P_binary(P,t):
    G=1.0
    M=0.5
    R=0.5
    x,y,v_x,v_y=P
    x1,x2,y1,y2=sun_position(R,t)
    r31=(sqrt((x-x1)**2+(y-y1)**2))**3
    r32=(sqrt((x-x2)**2+(y-y2)**2))**3
    a_x=(-G*M*(x-x1))/r31+(-G*M*(x-x2))/r32
    a_y=(-G*M*(y-y1))/r31+(-G*M*(y-y2))/r32
    return array([v_x,v_y,a_x,a_y])

def heun_orbit_binary(steps,h,x=3,y=0.,v_x=0., v_y=0.5): #x,y,v_x,v_y are default initial conditions
    R=0.5
    orbit=empty((steps,4))
    P=array([x,y,v_x,v_y])
    for i in xrange(steps):
        orbit[i]=P
        P_tilde=P+h*diff_P_binary(P,h*i)
        P+=(h/2)*(diff_P_binary(P,h*i)+diff_P_binary(P_tilde,h*i))
    return orbit

def plot_orbit(orbit):
    plot(orbit[:, 0], orbit[:, 1])

#Simulating Orbits
steps=5000
h=0.1
R=0.5

orbit_anim = heun_orbit_binary(steps, h,x=2,y=0.,v_x=0., v_y=0.7)
sun_orbit=empty((steps,4))
for i in xrange(steps):
    sun_orbit[i]=sun_position(R,h*i)
    
#Plotting and animating
fig, ax = subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.set_axis_bgcolor('k')
point, = plot([], [], 'ro',ms=6)
line, = plot([], [], 'cyan')
sun1_point, = plot([],[], 'yo', ms=12)
sun1_line, = plot([], [], 'cyan')
sun2_point, = plot([],[], 'yo', ms=12)
sun2_line, = plot([], [], 'cyan')
sizex = 5#1+abs(max(orbit_anim[:,0]))
sizey = 5#1+abs(max(orbit_anim[:,1]))
xlim(-sizex, sizex)
ylim(-sizey, sizey)

def init():
    point.set_data([], [])
    line.set_data([], [])
    sun1_point.set_data([], [])
    sun1_line.set_data([], [])
    sun2_point.set_data([], [])
    sun2_line.set_data([], [])
    return line, point, sun1_point, sun1_line, sun2_point, sun2_line,

def animate(i):
    point.set_data(orbit_anim[i, 0], orbit_anim[i, 1])
    line.set_data(orbit_anim[:i, 0], orbit_anim[:i, 1])
    sun1_point.set_data(sun_orbit[i,0],sun_orbit[i,2])
    sun1_line.set_data(sun_orbit[:i,0],sun_orbit[:i,2])
    sun2_point.set_data(sun_orbit[i,1],sun_orbit[i,3])
    sun2_line.set_data(sun_orbit[:i,1],sun_orbit[:i,3])
    return line, point, sun1_point, sun1_line, sun2_point, sun2_line,

ani=animation.FuncAnimation(fig, animate, init_func=init, frames=steps, interval=20, blit=True, repeat=True)
plot_orbit(orbit_anim)

#Now simulating many orbits for an array of initial x values and y velocities
end=7
initial_x1=linspace(0.6,1.8,end)
initial_v_y1=linspace(0.7,1.3,end)
initial_x2=linspace(2.0,3.2,end)
initial_v_y2=linspace(0.3,0.9,end)
steps=1000
h=0.1
i=1
figure(figsize=(10, 10))
xlim(-4,4)
ylim(-4,4)
for row in range(1, end + 1):
    for col in range(1, end + 1):
        orbit=heun_orbit_binary(steps,h,x=initial_x1[row-1],y=0.,v_x=0., v_y=initial_v_y1[col-1])
        subplot(end, end, i)
        plot_orbit(orbit)
        xticks([])
        yticks([])
        if i % end == 1:
            ylabel(str(initial_x1[row-1]))
        if i > end**2-end:
            xlabel(str(initial_v_y1[col-1]))
        i += 1
suptitle('Planetary Orbits for Different Initial Conditions (0.6<x<1.8, 0.7<$v_y$<1.3)')

i=1
figure(figsize=(10, 10))
xlim(-4,4)
ylim(-4,4)
for row in range(1, end + 1):
    for col in range(1, end + 1):
        orbit=heun_orbit_binary(steps,h,x=initial_x2[row-1],y=0.,v_x=0., v_y=initial_v_y2[col-1])
        subplot(end, end, i)
        plot_orbit(orbit)
        xticks([])
        yticks([])
        if i % end == 1:
            ylabel(str(initial_x2[row-1]))
        if i > end**2-end:
            xlabel(str(initial_v_y2[col-1]))
        i += 1
suptitle('Planetary Orbits for Different Initial Conditions (2.0<x<3.2, 0.3<$v_y$<0.9)')
show()