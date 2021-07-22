# Question Link: https://codeforces.com/problemset/problem/1323/A
for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    c = 0
    pos = []
    flag = False

    for j in range(n):
        if(arr[i] % 2 == 0):
            flag = True
            print(1)
            print(i+1)
            break
        else:
            c += 1
            pos.append(i+1)
            if c == 2:
                flag = True
                print(c)
                print(" ".join(str(e) for e in pos))
                break
    if(flag == False):
        print(-1)
