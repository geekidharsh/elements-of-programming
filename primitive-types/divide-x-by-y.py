def divide(x,y):
	'''
	idea is to look for the kth item in binary rep of x such that
	(2^k)y > x and (2^k-1)y <=x 
	and then
	add 2^k to the quotient and reduce x to x-2^k
	'''
	result = 0
	power = 32
	y_power =y<<power
	while x>=y:
		while y_power>x:
			y_power>>=1
			power-=1
		result += 1<<power
		x -= y_power
	return result


# test
# ------
print(divide(6,2))
print(divide(4,2))
print(divide(100,2))