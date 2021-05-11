class Solution:
    def checkDoorStatus(self, N):
        res = [0]*N
        for j in range(N):
            for i in range(1,N+1):
                if((j+1) % i == 0):
                    if(res[j] == 1):
                        res[j] = res[j] - 1
                    else:
                        res[j] = res[j] + 1
        return res

import math
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        ptr = ob.checkDoorStatus(N)
        print(*ptr)