if __name__ == "__main__":
    n, m = map(int,input().split())
    res = 0
    temp = 0

    res = m**(1/float(n))
    temp = res - int(res)

    if(temp == 0):
        print(int(res))
    else:
        print(-1)

    