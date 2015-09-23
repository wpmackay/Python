#William Mackay
#MTH 337 Assignment 3- Mayfly Population Model Analysis

from pylab import *

b=linspace(1,4,1000)
x=0.5
t_max=750
t_min=t_max/2
for i in xrange(t_max):
    if i>t_min:
        plot(b,x,'b.',ms=1,alpha=.3)
    x=b*(1-x)*x
    
show()
