def LifePath(st):
    # declaring sums
    year_sum = 0
    month_sum = 0
    day_sum = 0

    # sub sum 
    sub_year_sum = 0
    sub_month_sum = 0
    sub_day_sum = 0
    temp = 0

    # for year
    for i in range(0,4):
        year_sum = year_sum + int(st[i])
        if(year_sum > 10 and year_sum < 99):
            sub_year_sum = twoDigit(year_sum)
        else:
            sub_year_sum = year_sum

    # for month
    for i in range(4,6):
        month_sum = month_sum + int(st[i])
        if(month_sum > 10 and month_sum < 99):
            sub_month_sum = twoDigit(month_sum)
        else:
            sub_month_sum = month_sum

    # for day
    for i in range(6,8):
        day_sum = day_sum + int(st[i])
        if(day_sum > 10 and day_sum < 99):
            sub_day_sum = twoDigit(day_sum)
        else:
            sub_day_sum = day_sum

    total_sum = 0
    total_sum = sub_day_sum + sub_month_sum + sub_year_sum
    sub_total_sum = 0

    if(total_sum > 10 and total_sum < 99):
        sub_total_sum = twoDigit(total_sum)
        return int(sub_total_sum)
    else:
        return int(total_sum)

def twoDigit(x):
    temp = 0
    sum = 0
    while(x != 0):
        temp = x%10
        sum = sum + temp
        x = x/10
    
    return int(sum)

if __name__ == "__main__":
    s = "20000208"
    res = LifePath(s)
    print(res)