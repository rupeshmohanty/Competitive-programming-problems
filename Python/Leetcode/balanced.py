s = input()
r = 0
i = 0
c = 0

while i < len(s):
    if s[i] == 'R':
        r += 1
    else:
        r -= 1
    
    if r == 0:
        c += 1

    i += 1

print(c)