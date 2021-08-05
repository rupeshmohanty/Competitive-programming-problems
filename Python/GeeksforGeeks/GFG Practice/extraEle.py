def search(a,b,l,h):
    mid = (l + h) // 2
    if mid == h:
        return mid
    if(a[mid]==b[mid]):
        return search(a,b,mid+1,h)
    
    if(a[mid] != b[mid-1]):
        return mid

    return search(a,b,l,mid-1)

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(search(A,B,0,n-1))
