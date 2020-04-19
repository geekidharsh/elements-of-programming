# canConstruct ("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


# constraint: letter can be isLetterConstructible from magazine if all char in letter are present in magazine

# algorithm:
# # we walk through every unique char in letter and record its count
# then we walk through every char in magazine and see if it already exists in the letter count
# for each time a char is found we reduce the count till the char is gone
# at the end, if the letter count is zero/none, it means we have found all char in letters, in the magazine

# time: o(n+m)

def isLetterConstructible(letter, magazine):
	if not letter: #if letter is empty
		return True
	if not magazine: # if magazine is empty, letter cannot be constructed
		return False

	char_frequency_letter = {}
	for char in letter:
		if char not in char_frequency_letter:
			char_frequency_letter[char] = 1
		else:
			char_frequency_letter[char] += 1

	for char in magazine:
		if char in char_frequency_letter:# char found in magazine so we redece the count in char_frequency_letter by 1
			char_frequency_letter[char] -= 1
			if char_frequency_letter[char] == 0:
				del char_frequency_letter[char]
					
					if not char_frequency_letter: 
						# char frequency is empty {}, ie we've found all letter items in magazine
						return True
	return False


letter = 'aabbc'
magazine = 'aabbcde'

# letter = ''
# magazine = 'ab'

# letter = ''
# magazine = ''

print(isLetterConstructible(letter, magazine))


