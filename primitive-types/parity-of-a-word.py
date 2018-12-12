# Computing the partiy of a word
# parity of a binary word is 1 if the number of 1s in the word is odd; otherwise its 0.

# Write a program to compute the parity of very long word in 64-bit


# Tricks:
# ------
	# 1. x&(x-1) yield the lowest set bit of x
	# 2. x^=x>>32 
	# 	right shifts x by 32 bits and


def parity(x):
	# time complexity is O(n) for n is the size of input
	# input: 
	# x : a word in binary, can be 64-bit
	# return: 0 if parity is even or 1 if parity is odd.

	num_of_bits = {1:0, 0:0}
	while x:
		if x&1:
			num_of_bits[1] += 1
		x >>=1
	return num_of_bits[1]&1


def parity_optimized_bitfiddle(x):
	# input: 
	# x : a word in binary, can be 64-bit
	# return: 0 if parity is even or 1 if parity is odd.

	# time complexity is O(k) for k is the number of set bits aka 1 in the input

	result = 0
	while x: 
		result ^=x&1
		x = x&(x-1)
		#memorize this bit fiddle trick
		# details: 
		# Sample Input: integer representation of bit sequence 1111111110
		# Sample Output: 1111111100 after clearing the lowest set bit
		#
		# Technical Details: When counting in binary, the difference
		#    between two consecutive numbers (i.e. n and n-1) is twofold:
		#     1] The least significant set bit in the greater number
		#       is not set in the lesser number.
		#     2] All bits to the left of said least significant set bit
		#        are the same for both numbers.
	return result


def parity_table(x):
	# input: x a 64-bit number
	# Output; parity of x
	x^=








