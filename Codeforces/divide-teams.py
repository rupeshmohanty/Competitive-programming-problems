if __name__ == "__main__":
    q = int(input())

    for _ in range(q):
        n = int(input())
        arr = list(map(int,input().split()))
        res = []

        for i in range(n):
            for j in range(n):
                if(i != j):
                    if abs(arr[i] - arr[j]) == 1:
                        if (arr[i],arr[j]) not in res:
                            res.append((arr[i],arr[j]))
        
        if len(res) == 0:
            print(1)
        else:
            print(2)