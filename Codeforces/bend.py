if __name__ == "__main__":
    n = int(input())
    h = int(input())
    l = list(map(int,input().split()))
    width = 0

    for i in range(len(l)):
        if(l[i] > h):
            width = width + 2
        else:
            width = width + 1
    
    print(width)