arr = list(map(int,input().split()))
q = int(input())
queries = list(map(int,input().split()))
res = []
count = 0

i = 0
while(i < len(queries)):
    if count == q:
        break
    else:
        c = 0
        s = 0
        for j in range(queries[i],queries[i+1]+1):
            s += arr[j]
            c += 1
        count += 1
        res.append(s//c)

    i += 2

print(" ".join(str(e) for e in res))