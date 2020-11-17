import math

def CubeSum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + pow(i,3)
    
    return sum

if __name__ == "__main__":
    num = int(input("Enter the no. terms: "))
    res = CubeSum(num)
    print(res)
