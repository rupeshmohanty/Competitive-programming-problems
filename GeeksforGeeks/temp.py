n = int(input())
temp = []
count = 0

for i in range(n):
    t = input()
    temp.append(t)

s = input()
s.sort()

for i in temp:
    if i.sort() == s:
        count = count + 1

print(count)