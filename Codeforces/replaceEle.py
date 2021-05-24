if __name__ == "__main__":
    t = int(input())

    while(t > 0):
        n, d = map(int,input().split())
        arr = list(map(int,input().split()))
        count = 0

        for i in range(n):
            if(arr[i] > d):
                count += 1

        if(count > 0):
            print("NO")
        else:
            print("YES") 

        t -= 1