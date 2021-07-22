arr = list(map(int, input().split()))
s = list()

for i in range(len(arr)):
    if (arr[i],arr.count(arr[i])) not in s:
        s.append((arr[i],arr.count(arr[i])))

for j in range(len(s)):
    print(s[j][0],s[j][1])