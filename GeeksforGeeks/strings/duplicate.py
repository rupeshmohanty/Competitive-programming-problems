def duplicate(st):
    st = st.replace("Gfg","sub1",1)
    st = st.replace("Classes","sub2",1)

    st = st.replace("Gfg","It")
    st = st.replace("Classes","They")

    st = st.replace("sub1","Gfg")
    st = st.replace("sub2","Classes")
    
    return st


if __name__ == "__main__":
    s = "Gfg is best. Gfg also has Classes now. Classes help understand better."
    res = duplicate(s)
    print(res)
