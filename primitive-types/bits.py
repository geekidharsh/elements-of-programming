# The Operators:
# x << y
# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). 
# This is the same as multiplying x by 2**y.
	# ex: 2 or 0010, so 2<<2 = 8 or 1000.

# x >> y
# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
	# ex: 8 or 1000, so 8>>2 = 2 or 0010.


# x & y
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, 
# otherwise it's 0.

# x | y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, 
# otherwise it's 1.

# ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. 
# This is the same as -x - 1.

# x ^ y
# Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if 
# that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.




# https://www.hackerearth.com/practice/notes/bit-manipulation/

# bit fiddle trick is that: 
	# 1. numbers that are a power of 2, have only one bit set. 
		# all other numbers will have more than one bit set i.e 1 in more that one places 
		# in their binary representation
		# so 2, 4, 8, 16 etc. 

	# 2. binary representation of (x-1) can be obtained by simply flipping all the bits 
		# to the right of rightmost 1 in x and also including the rightmost 1.
		# so, x&(x-1) is basically, 
		# will have all the bits equal to the x except for the rightmost 1 in x.

	# 3. 


def number_of_bits(x):
	# as in number of set bits
	bits = 0
	while x:
		bits += x&1
		# right shift by 1 bit every move
		x >>=1
	return bits


def pos_of_bits(x):
	# input: integer
	output:  

	bit_pos = []
	bits = 0
	while x:
		bit_pos.append(x&1)
		x >>=1

	return ''.join([str(i) for i in reversed(bit_pos)])

print(pos_of_bits('a'))
