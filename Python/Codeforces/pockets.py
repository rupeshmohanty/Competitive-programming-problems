if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    max = 0

    for i in range(n):
        if(arr.count(arr[i]) > max):
            max = arr.count(arr[i])

    
    print(max)