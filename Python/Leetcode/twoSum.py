class Solution:
    def twoSum(self,numbers,target):
        i = 0
        j = len(numbers)-1
        while(i < len(numbers) and j != 0):
            if i != j:
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                elif numbers[i] + numbers[j] < target:
                    i += 1
                else:
                    j -= 1

numbers = list(map(int, input().split()))
target = int(input())
ob = Solution()
print(ob.twoSum(numbers, target))