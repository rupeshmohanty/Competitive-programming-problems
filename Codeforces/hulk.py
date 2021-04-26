if __name__ == "__main__":
    n = int(input())
    res = ""

    for i in range(1,n+1):
        if(i == n):
            if(n % 2 == 0):
                res = res + "I love it"
            else:
                res = res + "I hate it"
        else:
            if(i % 2 == 0):
                res = res + "I love that "
            else:
                res = res + "I hate that "

    print(res)
