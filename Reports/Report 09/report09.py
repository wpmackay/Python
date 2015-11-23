#Assignment 9- GPS System Simulation
#William Mackay
#MTH 337, Professor Adam Cunningham

from pylab import *

#"Satellite" Data in Meters
xi=array([5.53,4.44,0.045,6.67])
yi=array([2.23,8.45,.381,5.62])
d=array([2.72,3.63,6.75,1.77])

def stumbledown(f,p,stepsize,n=1000):
    nfails=0
    for i in xrange(n):
        q=[2*stepsize*rand()-stepsize+p[0],stepsize*rand()-(stepsize/2)+p[1]]
        if f(q)<f(p):
            plot([p[0],q[0]],[p[1],q[1]],'b.-')
            p=q
            nfails=0
        else: 
            plot([p[0],q[0]],[p[1],q[1]],'r-')
            nfails+=1
        if nfails>10:
            nfails=0
            stepsize=stepsize/2
        if stepsize<(10**-9):
            return p,i      
    

def GPS(X):
    xi=array([5.53,4.44,0.045,6.67])
    yi=array([2.23,8.45,.381,5.62])
    d=array([2.72,3.63,6.75,1.77])
    return sum((sqrt((X[0]-xi)**2+(X[1]-yi)**2)-d)**2)

figure(1)
axis([0,10,0,10])
for i in xrange(4):
    circle1=Circle((xi[i],yi[i]),d[i],color='k',fill=False)
    ax = gca()
    gca().add_artist(circle1)
    plot(xi[i],yi[i],'ko')
xlabel('x (m)')
ylabel('y (m)')
title('Satellite Positions')

p=[20,-20]
stepsize=.5

figure(2)
position,iterations=stumbledown(GPS,p,stepsize,n=2000)
for i in xrange(4):
    circle1=Circle((xi[i],yi[i]),d[i],color='g',fill=False)
    ax = gca()
    gca().add_artist(circle1)
xlabel('x (m)')
ylabel('y (m)')
title('Stumbledown Algorithm')

blue_line = Line2D([], [], color='blue', marker='.', label='Success')
red_line = Line2D([], [], color='red', label='Failure')
green_line = Line2D([], [], color='green', label='Satellite Circle')
legend(handles=[blue_line,red_line,green_line],loc='upper left')


print 'The position of the marker is:',position
print 'The stumbledown algorithm took',iterations,'steps to converge'

show()