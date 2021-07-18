for _ in range(int(input())):
    n,c0,c1,h = map(int,input().split())
    s = input()
    temp = c0*s.count('0') + c1*s.count('1')

    if c0 == c1:
        print(temp)
    elif c0 > c1:
        c = s.count('0')
        
        for i in range(n):
            if s[i] == '0':
                s = s.replace(s[i],'1')
        cost = c*h + s.count('1')*c1
        
        print(min(temp, cost))
    else:
        c = s.count('1')
        for i in range(n):
            if s[i] == '1':
                s = s.replace(s[i],'0')
        cost = c*h + s.count('0')*c0 
        
        print(min(temp, cost))
