'''
swap is done by comparing bits at position i and j in a arr(x)
	i and j are the ith and jth position bits in the binary representation of x in an array
		ex: x=9 and i=3, j=0
		so, bin representation of x in an array : 1 0 0 1, indices starting at 0 (typical array)

how the fuck, does this bit_mask work? 
		x= 8 and say, i=3, j=0
		so y = (1<<3)|(1<<0)
		i.e => y = 9
		now, 8 XOR 9 = 1
'''

	
def swap_bits(x,i,j):
	if x != 0:
		if (x>>i)&1 != (x>>j)&1:
			# bitwise & will compare the value of bits at lsb against 1
			# only if the values differ the program will enter if:
			bit_mask = (1<<i)|(1<<j)
			x^=bit_mask
			return x
		else:
			return 'swap not necessary'

	# time complexity is O(1) for any size of int


print(swap_bits(8,3,0))
