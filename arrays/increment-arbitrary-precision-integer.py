""""
Write a program that takes non negative array of digits, encoded to become an 
int digits returns D+1 in array. So, 
[1,2,9], 

ie. D = 129. D+1 = 130 ==> [1,3,0]

for numbers like 99, arr would overflow because given arr is only of length 2 whereas, 
return array is 100 or [1,0,0]
"""

def plus_one(A):
	# add 1 to the last element
	A[-1] += 1
	
	for i in reversed(range(1,len(A))):
		if A[i] == 10:
			A[i] = 0
			A[i-1] +=1
	if A[0] == 10:
		A[0] = 1
		A.append(0)

	return A


# time: O(n), n = len(A)
# space: O(1)

# test
print(plus_one([9,9,9]))
print(plus_one([1,2,9]))
print(plus_one([1,0,9]))
print(plus_one([9,9]))
print(plus_one([1,2,4]))