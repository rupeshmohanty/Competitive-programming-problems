class Solution:
    def maxArea(self, height):
        max_area = 0

        i = 0
        j = len(height) - 1
        while(i < len(height) and j != -1):
            if i != j:
                y = min(height[i],height[j])
                x = abs(j - i)
                
                if y*x > max_area:
                    max_area = y*x
                    j -= 1
            i += 1

        return max_area


height = list(map(int,input().split()))
ob = Solution()
print(ob.maxArea(height))