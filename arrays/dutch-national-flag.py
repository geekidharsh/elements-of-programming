""""
given an array and a pivot index k, make all items less than a[k] to the appear first 
and all greater than a[k] appear after a[k]

it's basically quicksort problem with a fixed given pivot index

input
[0,1,2,0,2,1,1]
# expected output for pivot_index 3
[0,0,1,2,2,1,1]
"""

def dutch_nat_flag(x, pivot_index):
	pivot = x[pivot_index]
	small = 0
	larger = len(x)-1

	for i in range(len(x)):
		# move all elements smaller than pivot
		if x[i] < pivot:
			x[i], x[small] = x[small], x[i]
			small +=1

	for i in reversed(range(len(x))):
		if x[i] > x[pivot]:
			x[i], x[larger] = x[larger], x[i]
			larger -=1
	return x


RED, WHITE, BLUE = range(3)

A = [0,1,2,0,2,1,1]
pivot_index = 3


print(dutch_nat_flag(A,pivot_index))
# time: O(n), space O(1) because operation happens in-place
