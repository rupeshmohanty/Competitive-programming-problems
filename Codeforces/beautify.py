if __name__ == "__main__":
    cord = []
    for i in range(1,6):
        arr = list(map(int,input().split()))
        ele = 1

        for j in range(1,6):
            if(arr[j-1] == ele):
                cord.append(i)
                cord.append(j)

    print(abs(3-cord[0]) + abs(3-cord[1]))
    

