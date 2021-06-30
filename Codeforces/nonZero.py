t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    s = sum(arr)
    count0 = arr.count(0)

    mod = s + count0

    if(mod == 0):
        print(count0+1)
    else:
        print(count0)
    