if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        a = []
        elements_to_remove = []
        n = int(input())

        a = list(map(int,input().split()))
        
        for j in range(n-1):
            if(abs(a[j] - a[j+1]) <= 1):
                if(a[j] < a[j+1]):
                    elements_to_remove.append(a[j])
                else:
                    elements_to_remove.append(a[j+1])
            else:
                continue
        
        for k in range(len(elements_to_remove)):
            a.remove(elements_to_remove[k])
        
        if(len(a) == 1):
            print("YES")
        else:
            print("NO")