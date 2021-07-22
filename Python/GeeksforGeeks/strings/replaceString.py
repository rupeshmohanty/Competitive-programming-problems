def replaceString(m,st1,st2):
    r = m.replace(st1,st2)

    return r

if __name__ == "__main__":
    main_str = input()
    s1 = input()
    s2 = input()
    res = replaceString(main_str,s1,s2)
    print(res)