def findAndCount(a,n):
    count = 0
    for i in range(n):
        if a[i] == '0':
            count += 1            

    return count

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    
    res = findAndCount(arr,n)
    print(n)