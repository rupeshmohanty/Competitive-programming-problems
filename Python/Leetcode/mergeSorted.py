class Solution:
    def merge(self,nums1,m,nums2,n):
        i = j = k = 0
        arr = []

        while(i < m and j < n):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        while(i < m):
            arr.append(nums1[i])
            i += 1
        
        while(j < n):
            arr.append(nums2[j])
            j += 1

        nums1.clear()

        nums1 += arr

nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
n = int(input())
ob = Solution()
ob.merge(nums1,m,nums2,n)
print(nums1)