x = input()
y = input()
t = ""

for i in x:
    if i in y:
        t += i

print(t)
for i in x:
    if i not in t:
        t += i

for i in y:
    if i not in t:
        t += i

print(len(t))