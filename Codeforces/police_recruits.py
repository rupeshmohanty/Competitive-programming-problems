if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    police_count = 0

    for i in range(n):
        if(a[i] == -1):
            if(police_count >= 1):
                police_count = police_count - 1
            else:
                count = count + 1
        else:
            police_count = police_count + a[i]
    
    print(count)
