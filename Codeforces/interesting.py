def checkSum(num,i):
    t = num + i
    temp = 0
    sum = 0

    while(t != 0):
        temp = t % 10
        sum += temp
        t = int(t/10)

    if(sum % 4 == 0):
        return True
    else:
        return False        

if __name__ == "__main__":
    a = int(input())
    fin = 0
    
    for i in range(0,10):
        res = checkSum(a,i)
        if(res):
            fin = i
            break
    
    print(a+fin)

    