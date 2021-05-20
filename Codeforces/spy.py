if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        
        for i in range(len(arr)):
            if(arr.count(arr[i]) == 1):
                print(i+1)
                break
