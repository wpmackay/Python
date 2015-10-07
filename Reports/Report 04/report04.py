#William Mackay
#MTH 337 Assignment 04

from pylab import *

#Part 1- Loading and Plotting Weather Balloon Data
data=loadtxt("balloon.dat", skiprows=138)
mins=data[:,0]
secs=data[:,1]
t=mins+(secs/60)
temp=data[:,5]

plot(t,temp,'b.')
xlabel('Time (mins)')
ylabel('Temperature (deg. C)')
title('Temperature vs. Time Measured by a Weather Balloon')

#Part 2- Finding machine epsilon, maximum float, and minimum float
def find_epsilon():
    n=0
    while True:
        x=2**(-n)
        if 1+x!=1:
            n+=1
        else:
            return 2**-(n-1)
def max_float():
    n=1.
    x=2.
    count=0
    while True:
        try: y=x**n
        except: 
            return x**(n-0.0005)
            break
        n+=0.0005
            
def min_float():
    n=1.
    x=2.
    while True:
        y=x**n
        #print '%e' % y
        if y==x**(n+1):
            return y
        else:
            n-=0.015
            
epsilon=find_epsilon()
minFloat=min_float()
maxFloat=max_float()

print 'Machine epsilon is',epsilon
print 'The smallest floating point number is', minFloat
print 'The largest floating point number is', maxFloat

show()