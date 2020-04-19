
def valid_palindrome(word):
	# we first store all counts of each letter in a dict
	# in order to be a valid palindrome: each letter must appear in pair, except for one in the middle: example: level, ll, ee, v
	word_count = {}
	for letter in word:
		if letter not in word_count:
			word_count[letter] = 1
		else:
			word_count[letter] += 1

	# iterator to generate sum of all pairs divided by 2
	# for a valid palindrome, there can only be one letter with no pair. i.e: v%2 <= 1 at most once, only.
	if sum(v%2 for v in word_count.values()) <=1:
		return True
	else: #not a valid palindrome
		return False


# time: o(n)
# space: o(c) where c is number of char in word

word = 'leve'
print(valid_palindrome(word))