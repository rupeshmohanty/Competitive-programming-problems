st = input()
patt = input()
min_index = len(st)

for i in patt:
    if i in st:
        if st.index(i) <= min_index:
            min_index = st.index(i)

if min_index < len(st):
    print(min_index)
else:
    print(-1)