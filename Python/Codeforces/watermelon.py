if __name__ == "__main__":
    w = int(input())
    count = 0

    for i in range(2,w,2):
        for j in range(2,w,2):
            if(i + j == w):
                count = count + 1
    
    if(count >= 1):
        print("YES")
    else:
        print("NO")