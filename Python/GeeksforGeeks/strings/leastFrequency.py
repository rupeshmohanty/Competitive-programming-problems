def leastFrequency(st):
    min = st.count(st[0])
    minimum_char = ""
    for i in st:
        if(st.count(i) < min):
            minimum_char = i

    return minimum_char

if __name__ == "__main__":
    s = input()
    res = leastFrequency(s)
    print(res)