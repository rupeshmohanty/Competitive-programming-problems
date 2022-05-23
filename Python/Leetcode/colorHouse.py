colors = list(map(int,input().split()))
m = 0

for i in range(len(colors)):
    for j in range(i+1,len(colors)):
        if colors[i] != colors[j]:
            if abs(i - j) >= m:
                m = abs(i-j)

print(m)