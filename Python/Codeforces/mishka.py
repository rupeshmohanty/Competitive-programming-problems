if __name__ == "__main__":
    n = int(input())
    mishka = 0
    chris = 0

    for i in range(n):
        a,b = map(int,input().split())

        if(a > b):
            mishka = mishka + 1
        elif(b > a):
            chris = chris + 1
        else:
            continue
    
    if(mishka > chris):
        print("Mishka")
    elif(mishka < chris):
        print("Chris")
    else:
        print("Friendship is magic!^^")
