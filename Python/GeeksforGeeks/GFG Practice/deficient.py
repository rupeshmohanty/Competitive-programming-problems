def divisorsSum(x):
    s = 0
    for i in range(1,x+1):
        if x % i == 0:
            s += i
    
    return s

x = int(input())
fac_sum = divisorsSum(x)
if fac_sum < 2*x:
    print("YES")
else:
    print("NO")