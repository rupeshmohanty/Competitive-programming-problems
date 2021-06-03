if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    max = arr[0]
    (res,i) = ([],0)

    if(len(set(arr)) == 1):
        count = 1
    else:
        while(i < n):
            temp = []    
            if(arr[i] > max):
                max = arr[i]
                temp.append(arr[i])
                i += 1
            else:
                i += 1

        res.append(temp)

    print(len(res))
