# Permutation means to rearrage a given list in a specific order
# Given an array A and a permutation array P, apply P to A.

# A = ['a','b','c','d']
# P = [2,0,1,3]
# Out: [b,c,a,d]


def permutation(A, P):
	A1 = []

	for i in P:
		A1.append(A[i])
	print(A1)




# test
A = ['a','b','c','d']
P = [2,0,1,3]



permutation(A, P)