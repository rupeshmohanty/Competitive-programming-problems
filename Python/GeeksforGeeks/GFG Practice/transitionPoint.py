n = int(input())
arr = list(map(int,input().split()))
res = 0
flag = False

for i in range(n):
    if arr[i] == 1:
        res = i
        flag = True
        break

if(flag):
    print(res)
else:
    print(-1)        