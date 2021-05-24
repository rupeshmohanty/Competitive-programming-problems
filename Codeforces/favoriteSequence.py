if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        res = []

        if(n == 1):
            print(str(arr[0]))
        else:
            # adding first elements to res and removing them from arr!
            res.append(arr[0])
            res.append(arr[n-1])

            for i in range(1,len(arr)-1):
                if(len(res) == n):
                    break
                else:
                    if(i != (n-i-1)):
                        res.append(arr[i])
                        res.append(arr[n-i-1])
                    else:
                        res.append(arr[i])
            
            print(" ".join(str(e) for e in res))

        