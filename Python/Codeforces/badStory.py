for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            flag = 1
            break
    
    if flag:
        print("No")
    else:
        print("Yes")
        i = 0
        while(i < len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if abs(arr[i] - arr[j]) not in arr:
                        arr.append(abs(arr[i]-arr[j]))
            i += 1
        
        print(len(arr))
        print(" ".join(str(e) for e in arr))
