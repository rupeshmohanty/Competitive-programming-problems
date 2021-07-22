if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n,x = map(int,input().split())
        sum = 2

        if(sum >= n):
            print(1)
        else:
            for i in range(n):
                sum = sum + x
                if(sum >= n):
                    print(i+2)
                    break