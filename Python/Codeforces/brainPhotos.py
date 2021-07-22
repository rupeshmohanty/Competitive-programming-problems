if __name__ == "__main__":
    n, m = map(int,input().split())
    color = 0

    for i in range(n):
        l = list(input().split())
        for j in range(m):
            if(l[j] == 'C' or l[j] == 'M' or l[j] == 'Y'):
                color = color + 1
    
    if(color > 0):
        print("#Color")
    else:
        print("#Black&White")

