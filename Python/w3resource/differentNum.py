def checkSeq(l):
	for i in l:
		if l.count(i) > 1:
			return False

	return True

if __name__ == "__main__":
	lt = list(map(int,input().split()))
	res = checkSeq(lt)

	if res:
		print("Yes all numbers are different!")
	else:
		print("No all numbers are not different!")