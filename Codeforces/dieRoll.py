if __name__ == "__main__":
    y, w = map(int,input().split())
    count = 0

    for i in range(1,7):
        if(i >= max(y,w)):
            count = count + 1
    
    
    if(6 % count == 0):
        print("1/" + str(int(6/count)))
    elif(count % 2 == 0):
        print(str(int(count/2)) + "/3")
    else:
        print(str(count) + "/6")