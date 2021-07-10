t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxm = max(arr) - arr[0]
    minm = min(arr) - arr[0]

    m = min(max(maxm,minm)+1, (n-1) - min(maxm, minm) + 1,(n-1) - maxm + minm + 2, (n-1) - minm + maxm + 2)

    print(m)
