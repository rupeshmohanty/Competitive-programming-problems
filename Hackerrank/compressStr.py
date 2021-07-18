# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
res = []
count = 0

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        res.append((count+1,int(s[i])))
        count = 0

print(" ".join(str(e) for e in res))