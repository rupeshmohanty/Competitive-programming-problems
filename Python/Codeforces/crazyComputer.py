n,c = map(int,input().split())
arr = list(map(int,input().split()))
count = 0

for i in range(0,n-1):
    if(arr[i+1] - arr[i] <= c):
        count += 1
    else:
        count = 0

print(count+1)