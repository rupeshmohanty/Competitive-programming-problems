# Question Link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
monthly_expenses = [2200,2350,2600,2130,2190]

# 1
print(monthly_expenses[1] - monthly_expenses[0])

# 2
print(monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2])

# 3
flag = False
for i in range(len(monthly_expenses)):
    if monthly_expenses[i] == 2000:
        flag = True

print(flag)

# 4
monthly_expenses.append(1980)
print(monthly_expenses)

# 5
monthly_expenses[3] = monthly_expenses[3] - 200
print(monthly_expenses)