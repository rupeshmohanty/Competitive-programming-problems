n = int(input())
arr = list(map(int,input().split()))
s = sum(arr)

if s % 3 == 0:
    print(1)
else:
    print(0) 