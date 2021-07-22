def evenRange(start,end):
	even = []
	for i in range(start,end):
		if(i % 2 != 0):
			even.append(i)

	return even

if __name__ == '__main__':
	a = int(input())
	b = int(input())

	res = evenRange(a,b)
	print(res)
