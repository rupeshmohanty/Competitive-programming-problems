if __name__ == "__main__":
    l = list(map(int,input().split()))
    temp = []

    for i in range(len(l)):
        if(l.count(l[i]) > 1):
            temp.append(l[i])
    
    temp_set = set(temp)

    if(len(temp) != 0):
        print(len(temp) - len(temp_set))
    else:
        print(0)