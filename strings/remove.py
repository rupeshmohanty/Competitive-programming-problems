def remove(arr,K):
    temp = ""
    for i in range(len(arr)):
        if(i != K):
            temp += arr[i]
    
    return temp

if __name__ == "__main__":
    l = input()
    k = int(input())
    res = remove(l,k)
    print(res)