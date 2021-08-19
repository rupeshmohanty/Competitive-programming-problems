def repeatedSub(A,B):
    if A == 0 or B == 0:
        return 0
    
    return 1 + repeatedSub(max(A,B) - min(A,B), min(A,B))

a,b = map(int,input().split())
res = repeatedSub(a,b)
print(res)