a = list(map(int,input().split()))
(f1,f2) = (0,0)
a.sort()

if(a[0] + a[1] + a[2] == a[3]):
    print("YES")
else:
    if(a[0] + a[3] == a[1] + a[2]):
        print("YES")
    else:
        print("NO")