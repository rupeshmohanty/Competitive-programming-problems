if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        p,a,b,c = map(int,input().split())
        m = a

        if(p % a == 0 or p % b == 0 or p % c == 0):
            print(0)
        else:
            print(min(a-p%a,b-p%b,c-p%c))