for _ in range(int(input())):
	s = input()
	flag = 0
	s += "a"

	if s != s[::-1]:
		print("YES")
		print(s)
	else:
		l = list(s)

		for i in range(1,len(l)):
			if l[i] == "a":
				l[i],l[i-1] = l[i-1],l[i]

			if l != l[::-1]:
				flag = 1
				break

		if flag:
			print("YES")
			print("".join(str(e) for e in l))
		else:
			print("NO")
