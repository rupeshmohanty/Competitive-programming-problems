if __name__ == "__main__":
    n = int(input())
    res = ""

    if(n % 2 != 0):
        print(-1)
    else:
        for i in range(1,n+1):
            if(i % 2 == 0):
                res += str(i-1) + " "
            else:
                res += str(i+1) + " "
    
    print(res)