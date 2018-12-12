# write a program that returns the nth fib number, also return the number in bits

# about fibonacci number: 
# 1. starting point can be either: 0 or 1. 
	# fib is: 0, 1, 1, 2, 3,5,8,13,21 and so on
	# so nth fib sequence. if n is 4 then fib(n) is 3

# non recursive solution
def fib(n):
	if n == 0 or n == 1:
		return n
	else:
		fib = [0,1] #initialize with 0,1 cos starting point of a fib sequence is known, obivously
		for i in range(2, n):
			fib.append(fib[i-2]+fib[i-1])
	return fib[n-1]



# recursive solution
def fib_recursive(n):
	if n == 0 or n == 1:
		return n
	else: 
		return fib_recursive(n-2)+fib_recursive(n-1)



# get bit of the number
def dec_to_bit(number):
	# dec to bit is base 2 to base 10
	dec = []

	if number == 0 or number == 1:
		return number
	else:
		while number>1:
			number = number//2
			print(number%2)
			# note: last bit is not showing, fix it

print(dec_to_bit(157))