def emptyData(a):
	return [x for x in a if x != '[]']

if __name__ == '__main__':
	arr = list(input().split())

	res = emptyData(arr)
	print(res)