num = int(input())
temp = []

while num > 0:
    temp.append(num%10)
    num = num // 10
temp = temp[::-1]
print(temp)
for i in temp:
    if temp.count(6) != 0:
        ind = temp.index(6)
        temp[ind] = 9
        break

st = ""

for i in temp:
    st += str(i)

print(int(st))