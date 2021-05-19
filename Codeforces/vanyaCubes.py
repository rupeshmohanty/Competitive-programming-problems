if __name__ == "__main__":
    n = int(input())
    tsum = 0
    h = 0

    while(tsum <= n):
        h += 1
        tsum += (h*(h+1))/2
    
    print(h-1)