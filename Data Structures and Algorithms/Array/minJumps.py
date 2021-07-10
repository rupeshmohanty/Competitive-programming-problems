def minJumps(arr,n):
    count = 0
    s = 0

    if arr[0] == 0:
        return -1
    else:
        i = 0
        while(i < n):
            if s <= n-1:
                s += arr[i]
                count += 1
            else:
                break
            
            i += arr[i]
        
        return count

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    res = minJumps(a, n)
    print(res)