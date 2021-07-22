def recursiveDeletion(st,sub):
    length = len(st)
    if sub in st:
        length = length - len(sub)
        st = st.replace(sub,"")
    else:
        return "No"
    
    if(length != 0):
        recursiveDeletion(st,sub_str)
    else:
        return "Yes"  

if __name__ == "__main__":
    s = input()
    sub_str = input()
    res = recursiveDeletion(s,sub_str)
    print(res)