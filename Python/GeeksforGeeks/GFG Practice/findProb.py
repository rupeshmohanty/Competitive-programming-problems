def findProb(num):
    if num == 1:
        return 1
    return num*findProb(num-1)

r = int(input())
g = int(input())
t = int(input())

tot = r + g + t
res = findProb(tot)
print(res)