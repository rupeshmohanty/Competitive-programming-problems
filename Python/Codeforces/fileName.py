if __name__ == "__main__":
    n = int(input())
    f = input()
    xcount = 0
    ans = 0

    for i in f:
        if(i == 'x'):
            if(xcount < 2):
                xcount += 1
            else:
                ans += 1
        else:
            xcount = 0

    print(ans)