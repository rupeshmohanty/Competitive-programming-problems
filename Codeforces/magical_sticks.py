if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())

        if(n%2 == 0):
            print(int(n/2))
        else:
            print(int(n/2)+1)
    