if __name__ == "__main__":
    n = int(input())
    s1 = input()
    s2 = input()
    (count,diff) = (0,0)

    for i in range(n):
        diff = abs(int(s1[i]) - int(s2[i]))
        count += min(diff,10 - diff)
    
    print(count)