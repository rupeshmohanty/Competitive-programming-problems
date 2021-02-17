def maxFrequency(st):
    max = st.count(st[0])
    maximum_char = ""

    for i in st:
        if(st.count(i) > max):
            maximum_char = i

    return maximum_char

if __name__ == "__main__":
    s = input()
    res = maxFrequency(s)
    print(res)