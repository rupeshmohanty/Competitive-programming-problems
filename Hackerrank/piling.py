for _ in range(int(input())):
	n = int(input())
	blocks = list(map(int,input().split()))
	stack = []
	flag = 0

	i = 0
	while(i < n//2):
		if i % 2 == 0:
			if blocks[n-i-1] > stack[-1]:
				flag = 1
				break
			else:
				stack.append(blocks[n-i-1])
		else:
			if blocks[i] > stack[-1]:
				flag = 1
				break
			else:
				stack.append(blocks[i])
		i += 1

	if flag:
		print("No")
	else:
		print("Yes")