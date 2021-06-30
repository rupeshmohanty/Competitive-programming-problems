def checkDistinct(a):
    res = []
    while(a > 0):
        temp = a%10
        res.append(temp)
        a = int(a/10)
    
    if(len(res) == len(set(res))):
        return True
    else:
        return False

if __name__ == "__main__":
    l,r = map(int,input().split())
    check = False
    ans = 0
    for i in range(l,r+1):
        check = checkDistinct(i)
        if(check):
            ans = i            
            break
        else:
            continue
    
    if(ans):
        print(ans)
    else:
        print(-1)
