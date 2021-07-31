# Question Link: https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen
def appendAndDelete(s,t,k):
    count = 0
    for i in s:
        if i not in t:
            s = s.replace(i, "")
            count += 1

    for i in t:
        if i not in s:
            s += i
            count += 1
    
    if count <= k:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    s = input()
    t = input()
    k = int(input())
    res = ""

    res = appendAndDelete(s,t,k)
    print(res)
