import math

r1 = int(input())
n = int(input())
r2 = int(input())
x = int(input())

th = math.ceil(x/60)

if th >= n:
    print(r1*(n) + r2*(th-n))
else:
    print(r1*th)