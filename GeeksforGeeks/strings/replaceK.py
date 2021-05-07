def replaceK(st,G,K):
    temp = st.find(G)

    for i in range(temp+1,len(st)):
        st = st[0] + st[1:].replace(G,K)

    return st

if __name__ == "__main__":
    s = input()
    g = input()
    k = input()
    res = replaceK(s,g,k)
    print(res)