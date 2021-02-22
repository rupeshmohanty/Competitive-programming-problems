def multipleWords(st,w,r):

    for i in range(len(st)):
        if st[i] in w:
            st[i] = r

    st = " ".join(st)

    return st

if __name__ == "__main__":
    s = "Geeksforgeeks is best for geeks and CS".split()
    word_list  = ["best","CS","for"]
    replace = "gfg"
    res = multipleWords(s,word_list,replace)
    print(res)