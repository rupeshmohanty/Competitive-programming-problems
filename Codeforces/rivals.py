t = int(input())

for _ in range(t):
    n,x,a,b = map(int, input().split())

    if x == 0:
        print(abs(a-b))
    else:
        print(min(n-1, abs(a-b) + x))