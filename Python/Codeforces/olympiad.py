n = int(input())
arr = list(map(int, input().split()))
(temp1,temp2,temp3) = ([],[],[])
(count1,count2,count3) = (0,0,0)

count1 = arr.count(1)
count2 = arr.count(2)
count3 = arr.count(3)

m = min(count1,count2,count3)
if m == 0:
    print(m)
else:
    print(m)
    for i in range(n):
        if arr[i] == 1:
            temp1.append(i+1)
        elif arr[i] == 2:
            temp2.append(i+1)
        else:
            temp3.append(i+1)
    
    for i in range(m):
        print(temp1[i],temp2[i],temp3[i])
    
    