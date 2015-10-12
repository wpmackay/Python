#William Mackay
#MTH 337- Assignment 5

from pylab import *

def linear_fit(x,y):
    alpha=mean(y)-mean(x)*((mean(x*y)-mean(x)*mean(y))/(mean(x**2)-mean(x)**2))
    beta=(mean(x*y)-mean(x)*mean(y))/(mean(x**2)-mean(x)**2)
    coeffs=[alpha,beta]
    return coeffs

def separation(m,n,b,t_max):
    s=empty(t_max)
    for i in xrange(t_max):
        m=b*(1-m)*m
        n=b*(1-n)*n
        s[i]=abs(m-n)
    return s

m=0.1
n1,n2,n3,n4=0.101,0.10001,0.101,0.1001
b1,b2,b3,b4=1.5,4.0,2.75,3.2
t_max=50
t=linspace(0,t_max,t_max)

s1=separation(m,n1,b1,t_max)
s2=separation(m,n2,b2,t_max)
s3=separation(m,n3,b3,t_max)
s4=separation(m,n4,b4,t_max)

figure(1)
semilogy(t,s1,'r.')
coeffs1=linear_fit(t[9:40],log(s1[9:40]))
bestfit1=coeffs1[1]*t+coeffs1[0]
semilogy(t,exp(bestfit1))
title('Separation Between Populations with Initial Conditions m=0.1 and n=0.101 When b=1.5')
xlabel('t (years)')
ylabel('Separation')

figure(2)
semilogy(t,s2,'r.')
coeffs2=linear_fit(t[0:20],log(s2[0:20]))
bestfit2=coeffs2[1]*t+coeffs2[0]
semilogy(t[0:20],exp(bestfit2[0:20]))
title('Separation Between Populations with Initial Conditions m=0.1 and n=0.10001 When b=4.0')
xlabel('t (years)')
ylabel('Separation')

figure(3)
semilogy(t,s3,'r.')
coeffs3=linear_fit(t[5:40],log(s3[5:40]))
bestfit3=coeffs3[1]*t+coeffs3[0]
semilogy(t,exp(bestfit3))
title('Separation Between Populations with Initial Conditions m=0.1 and n=0.101 When b=2.5')
xlabel('t (years)')
ylabel('Separation')

figure(4)
semilogy(t,s4,'r.')
coeffs4=linear_fit(t[15:40],log(s4[15:40]))
bestfit4=coeffs4[1]*t+coeffs4[0]
semilogy(t,exp(bestfit4))
title('Separation Between Populations with Initial Conditions m=0.1 and n=0.1001 When b=3.2')
xlabel('t (years)')
ylabel('Separation')

print coeffs1
print coeffs2
print coeffs3
print coeffs4

show()