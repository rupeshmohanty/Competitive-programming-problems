if __name__ == "__main__":
    n1,n2 = map(int, input().strip().split())
    hcf = 1

    for i in range(2,max(n1,n2)):
        if n1 % i == 0 and n2 % i == 0:
            hcf *= i
    
    print(hcf)