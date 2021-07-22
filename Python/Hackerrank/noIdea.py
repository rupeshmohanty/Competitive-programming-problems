n,m = map(int, input().split())
arr = list(map(int, input().split()))
h = 0

a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

for i in a:
    if i in arr:
        h += 1

for j in b:
    if j in arr:
        h -= 1

print(h)
