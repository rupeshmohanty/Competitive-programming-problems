prices = list(map(int, input().split()))
minm = min(prices)
min_pos = prices.index(minm)
maxm = 0

for i in range(min_pos,len(prices)):
    if prices[i] > maxm:
        maxm = prices[i]

print(maxm-minm)
