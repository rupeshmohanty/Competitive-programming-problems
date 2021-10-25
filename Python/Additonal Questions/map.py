n = int(input())
c = int(input())
l = []

for i in range(1,n+1):
    l.append(i)

i = 0
while len(l) != 0:
    if len(l) >= c:
        l.remove(i+c-1)
    else:
        break

    i += 1

print(l)