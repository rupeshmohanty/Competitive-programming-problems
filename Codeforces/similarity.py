t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = ""

    for i in range(0,2*n-1,2):
        res += s[i]
    
    print(res)
    

