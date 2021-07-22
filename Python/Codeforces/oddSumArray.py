if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        tsum = sum(arr)
        (e,o) = (0,0)

        if(tsum % 2 != 0):
            print("YES")
        else:
            for i in arr:
                if(i % 2 == 0):
                    e += 1
                else:
                    o += 1
            if(e >= 1 and o >= 1):
                print("YES")
            else:
                print("NO")
