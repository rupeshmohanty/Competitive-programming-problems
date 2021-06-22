if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n,m = map(int,input().split())
        count = 0

        for i in range(n):
            temp = input()

            for j in range(len(temp)):
                if(i == n-1):
                    if(temp[j] == "D"):
                        count += 1
                elif(j == m-1):
                    if(temp[j] == "R"):
                        count += 1
                
            
        print(count)