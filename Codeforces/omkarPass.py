t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if arr.count(arr[0]) == n:
        print(n)
    else:
        print(1)
        