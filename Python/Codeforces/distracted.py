t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = [s[0]]
    repeat = 0

    for i in range(1,n):
        if s[i] != s[i-1]:
            if s[i] not in res:
                res.append(s[i])
            else:
                repeat += 1
                break
    
    if repeat > 0:
        print("NO")
    else:
        print("YES")