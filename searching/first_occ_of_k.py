# questions:
# given a sorted array, find first occurance of item K, if it's in the array.
# return the index only.


# solution:
# 1. binary search can be used since, it's sorted array.
# 2. followed by walking backwards from item K to find it's first occurance



def first_occ_of_k(arr, K):
	left, right, result = 0, len(arr)-1, -1
	while left <= right:
		mid = (left + right) //2
		if arr[mid] == K:
			result = mid
			right = mid -1 # since now, right can never be equal to K
		elif arr[mid] < right:
			right = mid - 1
		else: # arr[mid] > right:
			left = mid + 1
	return result



arr = [-14,-10,2,108,108,243,285,285,285,401]

print(first_occ_of_k(arr, -14))