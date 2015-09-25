#William Mackay
#MTH 337 Assignment 3- Mayfly Population Model Analysis

from pylab import *

#Plotting transient behavior for different values of b
def mayfly_population(x_0,b,t,plot_string):
    x=[0]*(t)
    x[0]=x_0
    for i in xrange(1,t):
        x[i]=b*(1-x[i-1])*x[i-1]
    plot(range(t),x,plot_string)

t=25
x_0=0.5
b_transient=linspace(0,3,4)
color=['b','r','g','m']
figure(1)
for j in xrange(4):
    mayfly_population(x_0,b_transient[j],t,color[j])
xlabel('Time (years)')
ylabel('x')
title('Transient Behavior of Mayfly Population for b Values From 0 to 3')
legend1 = Line2D([], [], color='blue', label='b=0')
legend2 = Line2D([], [], color='red', label='b=1')
legend3 = Line2D([], [], color='green', label='b=2')
legend4 = Line2D([], [], color='magenta', label='b=3')
legend(handles=[legend1,legend2,legend3,legend4])

#Plotting asymptotic region of model for each b value
b=linspace(0,4,1000)
x=0.5
t_max=750
t_min=t_max/2

for i in xrange(t_max):
    if i>t_min:
        
        figure(2)
        plot(b,x,'b.',ms=1,alpha=.3)
        xlabel('b')
        ylabel('x')
        title('Asymptotic Behavior of Mayfly Population Model for b values from 0 to 4')
        
        figure(3)
        plot(b,x,'b.',ms=1,alpha=.3)
        xlim((3,4))
        xlabel('b')
        ylabel('x')
        title('Asymptotic Behavior of Mayfly Population Model for b values from 3 to 4')
    
    #Population Model
    x=b*(1-x)*x

show()
