def cap(st):
    for i in range(len(st)):
        if(st.count(st[i]) > 1):
            x = ""
            x += st[i].capitalize()
            st = st.replace(st[i],x)

    return st

if __name__ == "__main__":
    s = input()
    res = cap(s)
    print(res)