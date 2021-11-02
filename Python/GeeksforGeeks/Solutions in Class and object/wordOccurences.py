# Question Link: https://tcsxplore2020.blogspot.com/2020/02/python-code-solution.html
# Question 1
def count_words(s):
	l = s.split()
	d = {}

	for i in l:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1

	return d

def max_occurence_word(t):
	x = count_words(t)

	m = 0
	for i in x.values():
		if i > m:
			m = i

	ans = ""
	for j in x.keys():
		if x[j]==m:
			ans = j

	return ans 

t = input()
print(max_occurence_word(t))