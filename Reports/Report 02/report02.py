#William Mackay 
#MTH 337 Assignment 2- Non-prime C-Numbers

from pylab import *

#Function that checks whether or not an integer n is a c number. Checks that (b**n)%n=b for all b such that 1<b<n.
def is_C_number(n):
    b=range(1,n)
    count=0
    for i in xrange(0,n-1):
        if pow(b[i],n,n)==b[i]:
            count+=1
    if count==n-1:
        return True
    else:
        return False

#Function that checks whether or not an integer n is prime. Checks that number is not evenly divisible by any integer that is <=sqrt(n). 
def is_prime(n):
    for i in xrange(2,int(n**.5+1)):
        if n%i==0:
            return False
    return True

#Using is_prime and is_C_number to find non-prime C-numbers. Eliminates all primes and checks other numbers until a non-prime C-number is #found. Checks integers from 2 to 10000.
non_prime_C_numbers=0
n_max=10000
for i in xrange(1,n_max):
    if is_prime(i)==True:
        continue
    else:
        if is_C_number(i):
            non_prime_C_numbers=1
            print i
        else:
            continue
    if non_prime_C_numbers==1:
        print 'Yes, there is at least one non-prime C-number'
        break

if non_prime_C_numbers==0:
    print 'No non-prime C-numbers were found between 2 and',n_max
