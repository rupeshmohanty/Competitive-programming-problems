n = int(input())
arr = list(map(int,input().split()))
maxm = max(arr)
minm = min(arr)

print((maxm - minm + 1) - n)