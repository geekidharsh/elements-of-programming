def reverse_bits(x):
	unisgned_bit = 64
	arr = []
	rev = 0
	while x:
		arr.append(x&1)
		x>>=1

	# print(arr)
	n = len(arr)
	for i in range(n):
		rev += arr[n-i]*(2**i)
	return(rev)



print(reverse_bits(8))