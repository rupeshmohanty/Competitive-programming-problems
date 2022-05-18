nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
res = []

for i in nums1:
    if i in nums2:
        if i not in res:
            res.append(i)

print(res)
