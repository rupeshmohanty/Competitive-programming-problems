def isprime(a):
    c = 0
    for j in range(2,a):
        if(a % j == 0):
            c += 1
    
    if(c == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    x, y = map(int,input().split())
    count = 0

    for i in range(x+1,y+1):
        if(isprime(i)):
            if(i == y):
                count += 1
            else:
                count = 0
                break
    
    if(count == 1):
        print("YES")
    else:
        print("NO")