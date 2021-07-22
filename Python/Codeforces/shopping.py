if __name__ == "__main__":
    arr = list(map(int,input().split()))
    arr.sort()
    (minm,dist1) = (0,0)

    if(arr[0] == arr[1] and arr[1] == arr[2]):
        minm += 3*arr[0]
    else:
        dist1 += arr[0] + arr[1] + arr[2]
        minm += 2*(arr[0] + arr[1])

        if(dist1 < minm):
            minm = dist1

    print(minm)


    
