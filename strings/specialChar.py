def specialChar(st):
    st = st.replace(" ","")
    
    if(st.isalpha()):
        return "String is accepted"
    else:
        return "String is not accepted"

if __name__ == "__main__":
    s = input()
    res = specialChar(s)
    print(res)