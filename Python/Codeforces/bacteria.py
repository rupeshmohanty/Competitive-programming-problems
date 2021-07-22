import math

if __name__ == "__main__":
    n = int(input())
    x = 0

    if(n % 2 == 0):
        print(1)
    else:
        x = math.log((((n-1)/2)+1),2)
        print(int(x+1))