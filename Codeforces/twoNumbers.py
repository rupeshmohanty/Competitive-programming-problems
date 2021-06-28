if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    (a1,b1) = (0,0)

    for i in a:
        for j in b:
            if i + j not in a and i + j not in b:
                a1 = i
                b1 = j
    
    print(a1,b1)