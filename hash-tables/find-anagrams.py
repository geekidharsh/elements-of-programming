
words = ['elvis', 'levis', 'nap', 'pan', 'temp']

def findAnagrams(words):
	# returns indices in groups of anagram from words

	anagram_map = {}
	for i in range(len(words)):
		# first sort letters and store it in anagram_map
		s_word = ''.join(sorted(words[i]))
		if s_word not in anagram_map:
			anagram_map[s_word] = [i]
		else:
			anagram_map[s_word].append(i)
	return [group for group in anagram_map.values() if len(group) >= 2]

print(findAnagrams(words))


# time
# o(mnlogn) for each sorted and m is total each word in words