arr = [[10,20,30],[5,10,20],[2,4,6]]
res = [[0 for x in range(3)] for y in range(3)]
res[0][0] = arr[0][0]

for i in range(1,3):
    res[0][i] = arr[0][i] + res[0][i-1]
    for j in range(1,3):
        res[j][0] = res[j-1][0] + arr[j][0]

for i in range(1,3):
    for j in range(1,3):
        res[i][j] = res[i-1][j] + arr[i][j] + arr[i][j-1]

print(res)