if __name__ == "__main__":
    q = int(input())

    for _ in range(q):
        a,b,c = map(int,input().split())
        sum = 0
        temp = 0

        sum = a + b + c
        if(sum % 2 == 0):
            print(int(sum/2))
        else:
            temp = sum/2
            print(temp-1)