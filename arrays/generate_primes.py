# Take an integer argument 'n' and generate all primes between 1 and that integer n
# example: n = 18
# return: 2,3,5,7,11,13,17


def generate_primes(n):
	# run i, 2 to n
	# any  val between i to n is prime, store integer
	# remove any multiples of i from computation

	primes = []

	#generate a flag array for all element in 0 till n. initialize all items to True
	is_primes = [False, False] + [True]*(n-1) 

	for p in range(2,n+1):

		if is_primes[p]:
			primes.append(p)

			# remove all multiples of p
			for i in range(p,n+1,p):
				is_primes[i] = False

	return primes




print(generate_primes(35))






