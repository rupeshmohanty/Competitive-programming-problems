s = input()
k = int(input())

d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

sorted(d)
max_element = max(d)

for i in d:
    if k != 0:
        if d[i] > 1:
            d[i] -= 1
            k -= 1

s = 0
for i in d:
    s += pow(d[i],2)

print(s)