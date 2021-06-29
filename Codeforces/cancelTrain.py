t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    arrn = list(map(int,input().split()))
    arrm = list(map(int,input().split()))
    count = 0

    for i in arrn:
        if i in arrm:
            count += 1

    print(count)