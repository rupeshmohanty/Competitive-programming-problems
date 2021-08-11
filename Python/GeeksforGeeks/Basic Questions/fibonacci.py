n = int(input())
a = [0,1]

for i in range(2,n):
    x = a[i-1] + a[i-2]
    a.append(x)

print(" ".join(str(e) for e in a))