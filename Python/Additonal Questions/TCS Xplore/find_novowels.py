# Create a function with the name find_Novowels which takes a list of strings as input. The function checks each string of the list whether it has at least one vowel or not and returns another list containing the strings not having any vowel.

# Note:
# The check for the vowel should be case-insensitive .
# You can use the below sample input and output to verify your solution.

# Sample Input:

# 4
# almost
# vtyw
# sound
# prtwy

# Output:
# Strings without vowels:
# vtyw
# prtwy


# The first line in the sample input is the count of strings to be included in the list to be passed to the method find_Novowels .
# The strings are then provided one by one as the next lines of input.
# For more details, please refer to the below main section of code
# You can use the below sample main section to test your code.

# Solution!

def find_Novowels(l):
	no_vowels = []

	vowels = ['a','e','i','o','u']
	
	for i in l:
		flag = 0
		for j in vowels:
			if j in i:
				flag = 0
				break
			else:
				flag = 1

		if flag:
			no_vowels.append(i)
	
	return no_vowels

if __name__ == "__main__":
	st = list(map(str,input().split()))
	res = find_Novowels(st)

	print(res)
