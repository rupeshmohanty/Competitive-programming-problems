if __name__ == "__main__":
    t = int(input())

    for k in range(t):
        n,d = map(int,input().split())
        arr = list(map(int,input().split()))
        count = 0

        if(max(arr) <= d):
            print("YES")
        else:
            for i in range(n):
                for j in range(n):
                    if(i != j):
                        if(arr[i] + arr[j] <= d):
                            count += 1
            
            if(count == 0):
                print("NO")
            else:
                print("YES")