if __name__ == "__main__":
    a, b = map(int,input().split())
    res = 0

    for i in range(1,10):
        if(i*a % 10 == 0 or i*a % 10 == b):
            res = i
            break
        else:
            continue
    
    print(res)