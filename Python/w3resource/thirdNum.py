def thirdNum(l):
	while len(l) != 0:
		if len(l) >= 3:
			print(l[2])
			l.remove(l[2])
		else:
			l.remove(l[0])

if __name__ == "__main__":
	lt = list(map(int,input().split()))
	thirdNum(lt)



