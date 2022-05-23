nums = list(map(int,input().split()))
m = max(nums)
res = 0

for i in range(m,100):
    s = i
    flag = True
    for j in nums:
        s += j
        if s < 1:
            flag = False
            break
    
    if flag:
        res = i
        break

print(res)
