if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        a,b,k = map(int,input().split())
        c = 0

        if(k % 2 == 0):
            c += int((k/2))*(a-b)
        else:
            c += a*(int(k/2) + 1) - b*(int(k/2))
        
        print(c)