s = input()
count1,count2,count3 = 0,0,0

for i in s:
    if i == '(':
        count1 += 1
    elif i == ')':
        count1 -= 1
    elif i == '{':
        count2 += 1
    elif i == '}':
        count2 -= 1
    elif i == '[':
        count3 += 1
    else:
        count3 -= 1

if count1 == 0 and count2 == 0 and count3 == 0:
    print(True)
else:
    print(False)