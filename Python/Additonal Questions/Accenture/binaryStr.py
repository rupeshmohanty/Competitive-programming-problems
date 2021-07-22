# Accenture previous year questions!
def OperationsBinaryString(s):
    ans = 0
    n = len(s)

    if n == 0:
        return -1
    else:
        for i in range(0,n-2,2):
            if s[i+1] == 'C':
                ans = int(s[i])^int(s[i+2])
            elif s[i+1] == 'A':
                ans = int(s[i]) and int(s[i+2])
            else:
                ans = int(s[i]) or int(s[i+2])
            
        return ans

if __name__ == "__main__":
    s = input()
    res = OperationsBinaryString(s)
    print(res)