if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        x,y,z  = map(int,input().split())

        if(y != z):
            print("NO")
        else:
            print(x,x,z)
