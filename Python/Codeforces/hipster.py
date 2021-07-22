if __name__ == "__main__":
    a, b = map(int,input().split())
    count1, count2 = (0,0)

    if(a > b):
        a = a - b
        count1 = count1 + b
        count2 = count2 + int(a/2)
    else:
        b = b - a
        count1 = count1 + a
        count2 = count2 + int(b/2)

    print(count1,count2)
    
