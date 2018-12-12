'''
A = [3,3,1,0,2,0,1]
every ith entry is the max we can advance from i. 
write a program that advances such that it reaches the end of array A

'''


def advance_thru_array(A):

	furthest = 0
	last = len(A)-1
	i = 0
	while i<=furthest and furthest<last:
		furthest = max(furthest, A[i]+1)
		# since, from every position A[i], it can advance as furthest 
		# as i steps. that's why max of furthest and A[i]+1
		i += 1

	if furthest <= last:
		return True
		# if furthest is bigger than last, 
		# then the game for sure can advance till last, so it's a win
	else:
		return False

	# time complexity is O(n) and space is O(1)


A = [3,3,1,0,2,0,1]

print(advance_thru_array(A))
