if __name__ == "__main__":
    m = []
    steps = 0
    # getting a matrix input!
    for i in range(5):
        a = []
        for j in range(5):
            a.append(int(input()))
        m.append(a)
    
    for i in range(5):
        for j in range(5):
            if(m[i][j] == 1):
                i_position = i
                j_position = j

    steps = steps + abs(i_position - 2) + abs(j_position - 2)
    print(steps)
