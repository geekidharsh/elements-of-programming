import math

# solution 1
def palindrome_num(x):
	#brute force algorithm
	# considering x>0

	# complexity is O(n) where n is the number of digits in x
	# space complexity is O(n). 
	# idea: 
	# We can use log10 function to cut down space complexity to O(1)

	reverse = 0
	temp = x
	if x<=0:
		return 0
	else:
		try:
			while temp:
				reverse = reverse*10 + (temp%10)
				temp//=10
			if x == reverse:
				return True
			else:
				return False
		except e: 
			return e


# test
print(palindrome_num(11))
print(palindrome_num(2221))
print(palindrome_num(1221))
print(palindrome_num(-2221))





# solution 2: time: O(n), space: O(1)
def palindrome_optmized(x):

	if x<=0:
		return 0
	number_of_digits = math.floor(math.log10(x))+1
	msd_mask = 10**(number_of_digits-1)
	for i in range(number_of_digits//2):
		if x//msd_mask != x%10:
			return False
		else:
			x%=msd_mask #removes the msd in x
			x//=10 # removes the lsd in x
			msd_mask//=100 #100 because we are getting rid of 2 digits every operation, one from either side
	return True


# test
print(palindrome_optmized(121))
print(palindrome_optmized(111))
print(palindrome_optmized(1221))
print(palindrome_optmized(12214324325))








# scrap:
# # using an array
# 	while x:
# 		x_arr.append(x%10)
# 		x//=10
# 	for i in range(len(x_arr)//2):
# 		if x_arr[i] != x_arr[len(x_arr)-1-x]:
# 			state = False
# 		else:
# 			state = True
# 	return state