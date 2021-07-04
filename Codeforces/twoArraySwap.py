t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())),reverse=True)
    s = sum(a)

    for i in range(k):
        a[i],b[i] = b[i],a[i]
        if sum(a) < s:
            a[i],b[i] = b[i],a[i]
            break
        s = sum(a)

    print(sum(a))