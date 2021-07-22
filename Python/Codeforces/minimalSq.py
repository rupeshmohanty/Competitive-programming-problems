if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        a, b = map(int,input().split())
        res = 0

        for i in range(200):
            if(a > b):
                if(i >= a and i >= 2*b):
                    res = i*i
                    break
            elif(a == b):
                res = (2*a)*(2*b)
            else:
                if(i >= b and i >= 2*a):
                    res = i*i
                    break

        print(res)