n = int(input())
arr = list(map(int, input().split()))
s = set()

if 0 in arr:
    print("Yes")
else:
    temp = 0
    flag = 0

    for i in range(n):
        temp += arr[i]

        if temp == 0 or temp in s:
            flag = 1
        s.add(temp)
    
    if flag:
        print("Yes")
    else:
        print("No")