if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    temp = 0

    for i in range(n):
        temp = arr[i]

        if(temp < n):
            arr[i],arr[temp] = arr[temp],arr[i]
        
    
    print(" ".join(str(e) for e in arr))