for _ in range(int(input())):
    n,k = map(int,input().split())
    s = "a"*k
    
    for i in range(n-k):
        if s[-1] == "a":
            s += "c"
        elif s[-1] == "c":
            s += "b"
        else:
            s += "a"

    print(s) 

   