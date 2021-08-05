n = int(input())
arr = list(map(int,input().split())

for i in range(0,n-1,2):
    arr[i],arr[i+1] = arr[i+1],arr[i]

print(" ".join(str(e) for e in arr))