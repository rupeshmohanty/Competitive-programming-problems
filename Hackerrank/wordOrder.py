# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
res = []

for i in range(n):
    s = input()
    res.append(s)

s = set(res)
print(len(list(s)))

for i in s:
    print(res.count(i),end=" ")
