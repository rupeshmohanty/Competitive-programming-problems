n = int(input())
arr = list(map(int,input().split()))
arr.sort()
s = 0
res1,res2,res3 = 0,0,0

for i in range(n-2):
    if arr[i] + arr[i+1] > arr[i+2]:
        if arr[i] + arr[i+1] + arr[i+2] > s:
            res1,res2,res3 = arr[i],arr[i+1],arr[i+2]
            s = arr[i] + arr[i+1] + arr[i+2]

if res1 == 0 and res2 == 0 and res3 == 0:
    print(-1)
else:
    print(res1,res2,res3)