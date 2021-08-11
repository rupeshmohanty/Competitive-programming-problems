n,s = map(int,input().split())
res = []
for i in range(1,s-1):
    res.append(i)      

for i in range(len(res)):
    st = ""
    m = max(res)
    
    st += str(m) + str(12-m) + "0"*(n-2)
    
    if int(st) > 10**n:
        st = ""
        res.remove(m)

print(st)   