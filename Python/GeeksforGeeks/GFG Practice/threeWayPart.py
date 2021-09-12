n = int(input())
A = list(map(int, input().split()))
a,b = map(int,input().split())

temp = []

for i in A:
    if i < a:
        temp.append(i)

for j in A:
    if j >= a and j <= b:
        temp.append(j)

for k in A:
    if k > b:
        temp.append(k)

A.clear()
A += temp
print(A)
