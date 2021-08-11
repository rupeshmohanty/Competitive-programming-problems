d = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':5}
t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))    
    s = 0

    for i in range(n):
        if l[i] in list(d.keys()):
            s += d[l[i]]
    print(s)
    
        
    