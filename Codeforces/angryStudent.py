for _ in range(int(input())):
    n = int(input())
    s = input()
    mins = 0
    temp = "AP"

    for i in range(len(s)):
        if temp in s:
            mins += 1
            s = s.replace(temp,"AA")
    
    print(mins)
    