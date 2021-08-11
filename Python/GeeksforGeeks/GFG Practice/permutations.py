from itertools import permutations

a = input()
p = permutations(a)

for j in list(p):
    print("".join(str(e) for e in j))