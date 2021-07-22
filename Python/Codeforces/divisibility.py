if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        b, a = map(int,input().split())
        res = 0
        temp = 0

        if(b % a == 0):
            res = 0
        else:
            temp = b%a
            res = a - temp
    
        print(res)