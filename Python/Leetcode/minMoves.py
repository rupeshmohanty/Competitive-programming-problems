s = input()
c = 0
i = 0

while i < len(s):
    if s[i] == 'X':
        c += 1
        i += 3
    else:
        i += 1

print(c)
    