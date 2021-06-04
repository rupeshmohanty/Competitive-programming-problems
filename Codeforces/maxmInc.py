if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    max_count = 0

    
    for i in range(1,n):
        if(arr[i] > arr[i-1]):
            count += 1
        else:
            max_count = max(max_count, count)
        
    print(max_count)