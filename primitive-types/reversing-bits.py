# reverse the input unsigned integer and return
# so, 
# input: 10001100
# output: 00110001


# Easiest ways to do this is using: 
# bin() and int('1010', 2) functions

def reverse_bit(x):
	arr = ''
	if x>0:
		while x:
			arr+=str(x&1)
			x>>=1
		print(arr)
		return int(arr,2)
	else:
		print('non negative integer is not allowed')



def reverse_bits_optimized(x,bitsize):
	# x: a 32 bit integer
	# it is important to pre determined the bit size of the int

	result = 0
	for i in range(bitsize):
		result <<=1
		result |= x&1
		x>>=1
	# print(result)
	return result

print(reverse_bits_optimized(9,4))