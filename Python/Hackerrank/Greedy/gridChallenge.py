import math
import os
import random
import re
import sys

def gridChallenge(grid):
    # Write your code here
    check = 0
    for i in range(len(grid)):
        grid[i].sort()

    for i in range(0,len(grid)-1):
        if(grid[i+1] > grid[i]):
            check += 1
    
    if(check == len(grid) - 1):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)
