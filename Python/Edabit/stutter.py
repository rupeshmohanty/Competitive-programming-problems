# Question Link: https://edabit.com/challenge/gt9LLufDCMHKMioh2
def stuttering(st):
	r = ""

	i = 0
	while(i < 2):
		r += st[0] + st[1] + "... "
		i += 1

	r += st + "?"

	return r

if __name__ == "__main__":
	s = input()
	res = stuttering(s)
	print(res)