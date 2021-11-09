def is_curzon(num):
	if (2**num+1) % (2*num+1) == 0:
		return True
	else:
		return False

if __name__ == "__main__":
	n = int(input())
	res = is_curzon(n)
	print(res)