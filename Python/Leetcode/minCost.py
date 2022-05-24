cost = list(map(int,input().split()))
cost.sort(reverse=True)
s = 0

for i in range(0,len(cost)):
    if (i+1) % 3 == 0:
        continue
    else:
        s += cost[i]

print(s)