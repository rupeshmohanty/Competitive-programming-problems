def fragments(l, n):
	op_list = []
	i = 0
	while len(l) > n:
		op_list.append(l[i: i+n])
		l = l[n:]

	if(len(l) != 0):
		op_list.append(l)

	return op_list

if __name__ == '__main__':
	arr = list(map(int,input().split()))
	n = int(input())
	res = fragments(arr,n)
	print(res)