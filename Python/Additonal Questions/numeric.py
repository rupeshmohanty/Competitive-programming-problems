s = input()
sum = 0
num = "0"

for i in range(len(s)):
    if s[i].isnumeric():
        num += s[i]
    else:
        sum += int(num)
        num = "0"
sum += int(num)
print(sum)