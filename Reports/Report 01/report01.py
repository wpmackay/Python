#William Mackay, MTH 337, Fall 2015
#Finding Pythagorean triples for legs a and b between 1 and 5000

from pylab import *
ion

#Defining function to test whether or not a number 'n' is a perfect square
def is_square(n):
    m=n**.5
    if m%1==0:
        return True
    else:
        return False
    
# MTH 337, Fall 2015
# Created by Adam Cunningham, 9th September 2015
def test_is_square(n):
    '''Test the is_square function on all integers from 1 to n**2'''
    # Keep track of the number of incorrect results
    false_positives = 0
    false_negatives = 0
    for i in xrange(1, n):
    	# Check all integers in the interval [i**2, (i+1)**2 - 1]
        start = i**2
        # Check that the start of the interval is a perfect square
        if not is_square(start):
            false_negatives += 1
            print "Fails for perfect square", start
        # Check that the rest of the interval contains no perfect squares
        for j in xrange(start+1, (i+1)**2):
            if is_square(j):
                false_positives += 1
                print "Fails for non-perfect square", j
    end = n**2
    # Check that n**2 is a perfect square
    if not is_square(end):
        false_negatives += 1
        print "Fails for perfect square", end
    print '"is_square" returned', false_positives, "false positives,", false_negatives, "false negatives"

#Testing the "is_square" function
test_is_square(1000)    

#Defining function to find the greatest common divisor of two integers
def my_gcd(a,b):
    while a!=b:
        if b>a:
            (a,b)=(b,a)
        a=a-b
    return a

#Defining arrays for legs a and b
(a,b)=(range(1,5000),range(1,5000))
#Defining arrays to store legs and hypotenuses of pythagorean triples
(x,y,z)=([],[],[])

count=0
print "Progress: [",
#Finding the primitive pythagorean triples
for i in range(0,4999): #Outer loop from 1 to 5000
    for j in range(i,4999): #Start inner loop from i to avoid redundant pairs
        g=my_gcd(a[i],b[j])
        if g==1: #If GCD is 1, then check that a**2+b**2 is a perfect square
            n=(a[i]**2+b[j]**2)
            m=n**.5
            if is_square(n)==True: #If a**2+b**2 is a perfect square, then a,b,c is a primitive pythagorean triple  
                #Adding legs and hypotenuse of pythagorean triple to arrays x, y, and z
                x.append(a[i]) 
                y.append(b[j])
                z.append(m)
                count+=1
                if i%50==0:
                    print ".", #a[i],b[j],m                    
print "]" " Done." 

#Plotting figures
figure(0)
plot(x,y,'r.')
title('b vs. a')
xlabel('a (Short Leg)')
ylabel('b (Long Leg)')
draw()
figure(1)
plot(x,z,'b.')
title('c vs. a')
xlabel('a (Short Leg)')
ylabel('c (Hypotenuse)')
draw()
figure(2)
plot(y,z,'g.')
title('c vs. b')
xlabel('b (Long Leg)')
ylabel('c (Hypotenuse)')
draw()

#Printing number of primitive triples found
print count,"primitive Pythagorean triples were found."

show()
show()
show()


               