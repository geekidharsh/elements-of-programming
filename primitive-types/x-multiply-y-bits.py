def multiply_bits(x,y):
	
	running_sum = 0
	while x:
		if x&1:
			running_sum = add(running_sum,y)
		x>>=1
		y<<=1
	return running_sum


def add(a,b):
	# using bitwise operation, add two numbers a and b
	while b:
		carry = a&b
		a = a^b
		b = carry <<1
	return a

print(multiply_bits(80,10))


# time complexity is: O(n^2) because of n additions on n bits to perform a single multiplication
