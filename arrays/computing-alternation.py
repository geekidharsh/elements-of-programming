# desired pattern: 
# B[0] < B[1] > B[2] < B[3] > B[4] .... and so on

def computing_alternation(arr):
	arr = sorted(arr)
	i = 1
	while i < len(arr):
		temp = arr[i+1]
		arr[i+1] = arr[i]
		arr[i] = temp
		i +=2
	return arr

	# time complexity: O(nlogn) from sorted() + n operation in while loop
	# check solution online


def rearrange(arr):
	for i in range(len(arr)):
		arr[i:i+2] = sorted(arr[i:i+2], reverse= i%2)
	return arr
	# time complexity: O(n) 
	# book answer


# test inp
arr = [1,2,7,4,5,3,6]

# out_arr = [1,3,2,5,4,7,6]
print(computing_alternation(arr))

print(rearrange(arr))