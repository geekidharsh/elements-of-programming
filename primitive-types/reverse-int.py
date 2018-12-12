# given an int, return the reverse of itself.


# inp: 1234
# return: 4321
# perform operation on |x| and return along with the sign of x. using built in function abs()

def reverse_int(x):
	rev = 0
	x_remaining=abs(x)	
	while x_remaining:
		rev = 10*rev + x_remaining%10
		x_remaining //=10
	return -rev if x < 0 else rev

# time complexity is O(n) where n is the number of digits in x



print(reverse_int(-1234))

