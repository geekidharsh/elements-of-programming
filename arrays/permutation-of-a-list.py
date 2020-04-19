def permutation(A):
	if len(A) <2:
		return A

	permA = []

	for i in range(0,len(A)):
		m = A[i]
		remA = A[:i]
		print(remA)


permutation([1,2,3])