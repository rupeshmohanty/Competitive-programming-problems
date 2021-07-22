def shiftArray(l,pos):
	temp = []
	for i in range(pos):
		temp.append(l[i])

	for i in range(pos):
		l.remove(temp[i])

	resList = l + temp

	print(resList)

if __name__ == '__main__':

	arr = list(map(int,input().split()))
	d = int(input())
	n = int(input())

	res = shiftArray(arr,d)