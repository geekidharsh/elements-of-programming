
# ways to instantiate a list
A = [3,5,5,6,11]
B = [1]+[0]*10
C = list(range(20))


# binary search for sorted lists
import bisect
# This module provides support for maintaining a list in sorted order without having to sort 
# the list after each insertion. For long lists of items with expensive comparison operations, 
# this can be an improvement over the more common approach. 


# bisect(l,x) = locate the insertion point of x in l in order to maintain the sorted order
print(bisect.bisect(A,2))
print(bisect.bisect_left(A,6))
print(bisect.bisect_right(A,8))


# slicing

A1 = A[2:4]
# this means, in A, start from index 2 (or the 3rd element) and end at the 5th element but not include it


A2 = A[-1] # access last element

# use slicing to rotate a list
# -----------------------------

# left: 
# A[k:] + A[:k] rotates A by k to the left
A4 = A[2:] + A[:2] 

# right:
A5 = A[:-2]
print(A5)



# copy vs deepcopy


