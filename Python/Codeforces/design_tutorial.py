def checkComposite(a,b):
    res_a = False
    res_b = False

    for i in range(2,a):
        if(a % i == 0):
            res_a = True
    
    for i in range(2,b):
        if(b % i == 0):
            res_b = True

    if(res_a and res_b):
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())

    for i in range(1,n):
        x = i
        y = n-i
        res = checkComposite(x,y)
        if(res):
            break
        else:
            continue
    print(x,y)