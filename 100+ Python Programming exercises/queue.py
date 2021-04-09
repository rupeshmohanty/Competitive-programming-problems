if __name__ == "__main__":
    n = int(input())
    t = int(input())

    input_order = input()
    final_order = list(input_order)
    temp = ''

    for i in range(t):
        for j in range(len(final_order)-1):
            if(final_order[j] == 'B' and final_order[j+1] == 'G'):
                temp = final_order[j]
                final_order[j] = final_order[j+1]
                final_order[j+1] = temp

    res = "".join(final_order)
    print(res)