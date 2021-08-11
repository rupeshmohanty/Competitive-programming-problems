n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
res = 0

for i in a:
    if i not in b:
        res = i
        break

print(res)    