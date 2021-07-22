from math import gcd

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [n,n+1,n+2]
        temp = n
        s = 0

        while(temp != 0):
            s += temp%10
            temp = int(temp/10)
        
        i = 0
        while(i < len(arr)):
            res = gcd(arr[i], s)
            if res > 1:
                break
            s += 1
            i += 1
        
        print(arr[i])