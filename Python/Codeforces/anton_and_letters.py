if __name__ == "__main__":
    l = input()
    temp = []
    count = 0

    for i in l:
        if i != "{" and i != "," and i != "}" and i != " ":
            if i not in temp:
                temp.append(i)
        
    temp = set(temp)
    print(len(temp))