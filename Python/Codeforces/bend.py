if __name__ == "__main__":
    n, h = map(int, input().split())
    l = list(map(int,input().split()))
    width = 0

    for i in range(n):
        if(l[i] > h):
            width = width + 2
        else:
            width = width + 1
    
    print(width)