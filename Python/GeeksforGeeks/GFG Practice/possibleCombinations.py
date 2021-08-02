# Question Link: https://www.geeksforgeeks.org/python-program-to-print-all-possible-combinations-from-the-three-digits/
from itertools import permutations

comb = permutations([1,2,3],3)

for i in comb:
    print(i)