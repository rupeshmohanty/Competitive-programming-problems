n = int(input())
arr = list(map(int,input().split()))
res = []

for i in range(3):
    temp = 0
    j = i
    
    while(j < n):
        temp += arr[j]
        j += 3

    res.append(temp)

if(res[0] > res[1] and res[0] > res[2]):
    print("chest")
else:
    if(res[1] > res[2]):
        print("biceps")
    else:
        print("back")        