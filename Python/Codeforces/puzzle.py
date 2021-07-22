if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n,m = map(int,input().split())
        
        if(n == 1 or m == 1):
            print("YES")
        else:
            if(n == 2 and m == 2):
                print("YES")
            else:
                print("NO")