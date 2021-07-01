t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    s = sum(arr)

    print(s-1)