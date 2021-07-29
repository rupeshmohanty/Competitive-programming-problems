n,k = map(int,input().split())

res = 0
imp = []

for i in range(n):
    a,b = map(int,input().split())
    if b == 0:
        res += a
    else:
        imp.append(a)
    
    imp.sort(reverse=True)

    # picking k terms!
    res += sum(imp[0:k])

    # next k terms are to be deleted!
    res -= sum(imp[k:0])

    print(res)
