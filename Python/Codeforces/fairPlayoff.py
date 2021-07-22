if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        s1,s2,s3,s4 = map(int,input().split())
        (max1,max2) = (max(s1,s2),max(s3,s4))
        count = 0 

        if(max1 == s1):
            if(s2 > max2):
                count += 1
        else:
            if(s1 > max2):
                count += 1
        
        if(max2 == s3):
            if(s4 > max1):
                count += 1
        elif(max2 == s4):
            if(s3 > max1):
                count += 1
        
        if(count == 0):
            print("YES")
        else:
            print("NO")


    


