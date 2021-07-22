t = int(input())

for _ in range(t):
    a = input()
    b = input()
    c = input()
    flag = 0

    for i in range(len(a)):
        if c[i] != a[i] and c[i] != b[i]:
            flag = 1
            break
    
    if flag == 1:
        print("NO")
    else:
        print("YES")