if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    
    # sorting the array to get the highest quantity of burle a citizen has!
    arr.sort()

    for i in range(n):
        count = count + arr[n-1] - arr[i]
    
    print(count)
    