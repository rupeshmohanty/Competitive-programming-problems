if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        res = []
        count = 0

        for i in range(len(arr)):
            for j in range(len(arr)):
                if(i != j):
                    if abs(arr[i] - arr[j])/2 not in res:
                        res.append(abs(arr[i] - arr[j])/2)
                        count += 1
                
        print(count)