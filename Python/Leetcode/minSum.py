num = int(input())
res = []

while num > 0:
    res.append(num%10)
    num = num // 10

res.sort()
temp = []

for i in range(len(res)-2):
    temp.append(res[i]*10+res[i+2])

print(sum(temp))
