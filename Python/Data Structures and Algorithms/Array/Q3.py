# Question Link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
odd = []
m = int(input())

for i in range(1,m):
    if i % 2 != 0:
        odd.append(i)

print(odd)