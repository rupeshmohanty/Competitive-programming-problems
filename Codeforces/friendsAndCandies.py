if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        (av,c) = (0,0)
        
        if(sum(arr) % n == 0):
            if(n == 1):
                print(0)
            elif(arr.count(arr[0]) == n):
                print(0)
            else:
                av = int(sum(arr)/n)
                
                for i in range(n):
                    if(arr[i] > av):
                      c += 1

                print(c)  
        else:
            print(-1)