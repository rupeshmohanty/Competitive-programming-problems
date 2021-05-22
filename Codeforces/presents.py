if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    
    if(n % 2 == 0):
        for i in range(n-2):
            arr[i],arr[i+2] = arr[i+2],arr[i]
    else:
        pass

    print(" ".join(str(e) for e in arr))