def Concatenate(l):
    temp = []
    r = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if(i+1 < len(l[i])):
                temp.append(l[i][j] + l[i+1][j])
            
    r.append(temp)

    return r

if __name__ == "__main__":
    test_list = [["Gfg","good"], ["is", "for"]]
    res = Concatenate(test_list)
    print(res)