s = input()
t = ""
t += s[0]

for i in range(1,len(s)):
    if s[i].isupper():
        t += " "
    t += s[i]

print(t.lower())
