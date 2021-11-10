def wordFreq(st):
	l = s.split()
	words = {}

	for i in l:
		if i in words:
			words[i] += 1
		else:
			words[i] = 1

	return words

if __name__ == "__main__":
	s = input()
	freq = wordFreq(s)

	for i in list(freq.keys()):
		print(f'{ i }:{ freq[i] }')
	