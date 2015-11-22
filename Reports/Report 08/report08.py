#William Mackay
#MTH 337 Assignment 8

from pylab import *

n=10000

#Part 1 - Random Number Generation

def RNG(k, a=427419669081, m=999999999989):
    k=a*k%m
    xk=k/m
    return xk

def randu(k, a=2**16+3, m=2**31):
    k=a*k%m
    xk=k/m
    return xk

#Histogram for uniformity of RNG
k_rng=linspace(1,999999999989,n)
x_rng=RNG(k_rng)

figure (1)
hist(x_rng,50)
title('RNG Histogram')

#Testing for pairwise correlation in RNG
figure(2)
plot(x_rng[0::2],x_rng[1::2],'b.')
title('RNG Pairwise Correlation')
xlabel('$x_i$')
ylabel('$x_{i+1}$')

#Histogram for uniformity of randu
k_randu=linspace(1,2**31,n)
x_randu=randu(k_randu)

figure (3)
hist(x_randu,50)
title('randu Histogram')

#Testing for pairwise correlation in randu
figure(4)
plot(x_randu[0::2],x_randu[1::2],'b.')
title('randu Pairwise Correlation')
xlabel('$x_i$')
ylabel('$x_{i+1}$')

#Testing random.rand
x_rand=rand(n)

figure (5)
hist(x_rand,50)
title('random.rand Histogram')

figure (6)
plot(x_rand[0::2],x_rand[1::2],'b.')
title('random.rand Pairwise Correlation')
xlabel('$x_i$')
ylabel('$x_{i+1}$')

#Part 2 - Finding the Mean of mysterf Using Monte Carlo Integration
print "PART 2"

from mystery import mysteryf

x=5*rand(1000)
y=mysteryf(x)

figure (7)
plot(x,y,'b.')
title('Plotting mysteryf Evaluated at Random Points')
xlabel('x')
ylabel('mysteryf(x)')

def mysteryf_mean(n):
    x=5*rand(n)
    y=mysteryf(x)
    y_avg=mean(y)
    return y_avg

y_avg=mysteryf_mean(n)
print "The mean of mysteryf in the range [0,5] is",y_avg

#Part 3 - Monte Carlo Integration of a Polar Function
print "PART 3"

theta=linspace(0,2*pi,400)
r=2+cos(7*theta)

#Defining box enclosing function
x=6*rand(n)-3
y=6*rand(n)-3
total_area=6**2

#Converting to polar coordinates
theta2=arctan2(y,x)
r2=sqrt(x**2+y**2)

#Plotting function and box
figure(8)
polar(theta,r,'k',linewidth=2)
polar(theta2,r2,'b.',ms=1, alpha=0.5)
title(r'$r=2+cos(7\theta)$ With Random Points')

#Finding r of the actual function at each random theta value
rf=2+cos(7*theta2)
#Calculating number of points inside the curve
inside=(rf-r2)>=0
inside=sum(inside)

#Using ratio of points inside to total to find area of the curve
area_ratio=float(inside)/n
area_curve=area_ratio*total_area
print "The area of the curve is approximately",area_curve

#Part 4 - Simulating a Bernoulli Random Number
print "PART 4"

num_swings=100
num_hits=29
p=0.29

def batting_trial(num_swings,num_hits,p,n):
    swings=rand(n,num_swings)
    hits=swings<p
    hits_per_trial=sum(hits,axis=1)
    x=float(sum(hits_per_trial==num_hits))  
    return x/n

prob=batting_trial(num_swings,num_hits,p,n)
print "The probability of getting exactly 29 hits is approximately",prob

#Part 5 - Sums of Random Numbers, and the Central Limit Theorem

figure(9)
ylim([0,1.5])
for i in xrange(2,9):
    results=rand(i,n)
    totals=sum(results, axis=0)
    hist(totals,bins=50, normed=True,histtype='step',label=str(i))
title('Histograms of Sums of 2-8 Random Numbers')
legend()

figure(10)
for i in xrange(2,9):
    results=rand(i,n)
    totals=sum(results, axis=0)
    hist((totals-(i/2.))/(sqrt(i)),bins=50, normed=True,histtype='step',label=str(i))
title('Histograms of Sums of 2-8 Random Numbers shifted by M/2 and Divided by $M^{1/2}$')
legend()

u = rand(n*10)
v = (32*u)**(1./5)
figure(11)
hist(v, normed=True, bins=50, fc='c', label='v = g(u)')
x = linspace(0, 2, 400)
y = (5./32)*x**4
plot(x, y, 'r', lw=2, label='p(v)')
xlabel('v')
legend(loc='upper left')

figure(12)
ylim([0,1.5])
for i in xrange(2,9):
    results=(32*(rand(i,n)))**(1./5)
    totals=sum(results, axis=0)
    hist(totals,bins=50, normed=True,histtype='step',label=str(i))
title('Histograms of Sums of 2-8 Non-Uniform Random Numbers')
legend()

#Part 6 - Stock Market Simulation
print "PART 6"

def stock_sim(s_0,t,mu=0,sigma=0.05,trials=1):
    s=empty((trials,t))
    s[:,0]=s_0*ones(trials)
    for i in xrange(1,t):
        epsilon=normal(size=trials)
        s[:,i]=(1+mu+sigma*epsilon)*s[:,i-1]
    return s

s_0=1
mu=0.000
sigma1=0.05
sigma2=0.01
t_max=365
trials=10000
t=linspace(0,t_max,t_max)
s1=stock_sim(s_0,t_max,mu,sigma1,trials)
s2=stock_sim(s_0,t_max,mu,sigma2,trials)

t=linspace(0,t_max,t_max)
s=stock_sim(s_0,t_max,mu,sigma1,5)

figure(13)
for i in xrange(5):
    plot(t,s[i,:],label=str(i))
title('Several Runs of stock_sim for 1 Year')
    
final_price1=s1[:,364]
EV1=mean(final_price1)
loss1=final_price1<1
p_loss1=float(sum(loss1))/trials
print "Expected Value","(", u'\u03c3',"= 0.05",")","=", EV1
print "Probability of Losing Money =", p_loss1
figure(14)
hist(final_price1,50)
title(r'Histogram of Final Stock Price $(\sigma=0.05)$')

final_price2=s2[:,364]
EV2=mean(final_price2)
loss2=final_price2<1
p_loss2=float(sum(loss2))/trials
print "Expected Value","(", u'\u03c3',"= 0.01",")","=", EV2
print "Probability of Losing Money =", p_loss2
figure(15)
hist(final_price2,50)
title(r'Histogram of Final Stock Price $(\sigma=0.01)$')

show()