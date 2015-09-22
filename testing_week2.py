# MTH 337, Fall 2015
# Testing the "is_square" function
# Created by Adam Cunningham, 9th September 2015

def is_square(n):
    m=n**.5
    if m%1==0:
        return True
    else:
        return False

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
    
