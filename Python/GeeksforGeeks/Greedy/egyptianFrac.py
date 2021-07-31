# Question Link: https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/
import math

nr = int(input())
dr = int(input())
res = []
temp = math.ceil(dr/nr)

res.append("1/"+str(temp))

while(nr > 0):
    nr = nr*temp - dr
    dr = dr*temp
    if nr > 0:
        res.append(str(nr) + "/" + str(dr))

print(" + ".join(str(e) for e in res)) 