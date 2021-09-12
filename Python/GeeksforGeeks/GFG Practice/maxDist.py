n = int(input())
arr = list(map(int,input().split()))
m = 0

i,j = 0,0

while i < len(arr):
    temp = arr[i]
    j = arr.index(temp)
    
    if abs(j-i) > m:
        m = abs(j-i)
    
    i += 1

print(m)