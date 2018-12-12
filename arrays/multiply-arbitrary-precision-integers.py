""""
Write a program that takes 2 array of digits, returns their product
A x B = AB
"""

def multiply(A,B):

	sign = -1 if ((A[0]<0) ^ (B[0]<0)) else 1

	# get modulus numbers for the values at index 0
	A[0], B[0] = abs(A[0]), abs(B[0])

	result = [0]*(len(A)+len(B))
	for i in reversed(range(len(A))):
		for j in reversed(range(len(B))):
			result[i+j+1] += A[i]*B[j]
			result[i+j] += result[i+j+1] // 10
			result[i+j+1] %= 10

	# remove leading zeros
	for i in range(len(result)):
		if i:
			result=result[i:]
			break

	# add sign to result[0]
	result[0] = result[0]*sign
	return result


# test
print(multiply([-1,1,0],[-8,8]))
print(multiply([-1,1,0],[8,8]))
print(multiply([1,2,0],[8,8])) #fails