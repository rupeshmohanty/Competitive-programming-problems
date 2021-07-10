n = int(input())
a = list(map(int, input().split()))
s = " ".join(str(e) for e in a)

for i in range(len(s)):
    if s[i] != ' ':
        if int(s[i]) % 2 == 0:
            s = s.replace(s[i], str(int(s[i]) - 1))
        else:
            s = s.replace(s[i], str(int(s[i]) + 1))
    
print(s)
