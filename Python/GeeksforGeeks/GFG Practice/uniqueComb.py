# Question Code: https://www.geeksforgeeks.org/python-program-to-get-all-unique-combinations-of-two-lists/
import itertools
from itertools import permutations

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

uniq_comb = []

permut = permutations(list1, len(list2))

for i in permut:
    zipped = zip(i,list2)
    uniq_comb.append(list(zipped))

print(uniq_comb)