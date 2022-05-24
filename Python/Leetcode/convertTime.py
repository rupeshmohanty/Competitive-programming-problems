current = input()
correct = input()

cur_hr = int(current[0:2])
cor_hr = int(correct[0:2])

cur_min = int(current[3:5])
cor_min = int(correct[3:5])

tot_cur = cur_hr*60 + cur_min
tot_cor = cor_hr*60 + cor_min
temp = tot_cor - tot_cur
c = 0

while temp > 0:
    if temp >= 60:
        c += temp // 60
        temp = temp % 60
    elif temp >= 15:
        c += temp // 15
        temp = temp % 15
    elif temp >= 5:
        c += temp // 5
        temp = temp % 5
    else:
        c += temp // 1
        temp = temp % 1

print(c)