if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        s = ""

        for i in range(2,n+1):
            s += str(i) + " "
        
        s += str(1)

        print(s)

