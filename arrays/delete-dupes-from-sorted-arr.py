def delete_dupes_from_sorted_1(arr):
	# time O(n) space O(1)

	# count number of valid entries
	i = 1


	for j in range(1, len(arr)):
		if arr[i-1] != arr[j]:
			arr[i] = arr[j]
			i += 1
	# resulting arr will still have invalid items but theres no 
	# requirement of the code to delete items beyond the last valid item
	return arr, i

	# optionally
	# to get all valid items only, use slice: arr[:i]











# test
arr = [2,3,5,5,7,11,11,11,13] # inp
# exp out: ([2, 3, 5, 7, 11, 13, 11, 11, 13], 6)

print(delete_dupes_from_sorted_1(arr))