#William Mackay
#Assignment 7- Newton's Method in the Complex Plane

from pylab import *

#Using 1000 points for increased resolution
npts = 1000
#Creating meshgrid of imaginary points
x = linspace(-1, 1, npts)
y = linspace(-1j, 1j, npts)
X, Y = meshgrid(x, y)
Z = X + Y

#Defining the three roots and the tolerance 
r1 = complex(1, 0)
r2 = complex(-.5, sqrt(3)/2.)
r3 = complex(-.5, -sqrt(3)/2.)
tol = 1e-6

#Run newton's method for 10 iterations
niters = 20
for i in xrange(niters):
    Z -= (Z**3 - 1)/(3*Z**2)

#Points are colored red if they converged to the first root, green for the second, and blue for the third.
reds = abs(Z - r1) < tol
greens = abs(Z - r2) < tol
blues = abs(Z - r3) < tol
#Generating an array for the image
img = zeros((npts, npts, 3))
img[:,:,0] = reds
img[:,:,1] = greens
img[:,:,2] = blues
#Shwing the first image
figure(1)
imshow(img[::-1])

#Running a modified version of the previous code whihc encodes the nuber of iterations into the coloring of the image
#Fewer points are used because this code is less efficient
npts = 500
x = linspace(-1, 1, npts)
y = linspace(-1j, 1j, npts)
X, Y = meshgrid(x, y)
Z = X + Y

r1 = complex(1, 0)
r2 = complex(-.5, sqrt(3)/2.)
r3 = complex(-.5, -sqrt(3)/2.)
tol = 1e-6

#Added nested for loop to newton's method code which increases the count for each iteration in which the value has not coveged
count=zeros((npts,npts))
niters = 20
for i in xrange(niters):
    Z -= (Z**3 - 1)/(3*Z**2)
    for j in xrange(npts):
        for k in xrange(npts):
            if abs(Z[j,k] - r1) > tol and  abs(Z[j,k] - r2) > tol and  abs(Z[j,k] - r3) > tol:
                count[j,k]+=1
#Normalizing the count by dividing by the maximum value. Each element should be between 0 and 1 now.                
count=count/amax(count)
reds = abs(Z - r1) < tol
greens = abs(Z - r2) < tol
blues = abs(Z - r3) < tol
img = zeros((npts, npts, 3))
#Multiplying color values by count so that the more iterations, the brighter the color.
img[:,:,0] = reds*(count)
img[:,:,1] = greens*(count)
img[:,:,2] = blues*(count)
figure(2)
imshow(img[::-1])

show()



