if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        r,b,d = map(int,input().split())
        
        if(b > r*(d+1)):
            print("NO")
        else:
            print("YES")