def Convert(string):
    return list(string)

if _name_ == "_main_":
    n, t = map(int, input().split())

    input_order = input()
    final_order = Convert(input_order)
    temp = ''

    for i in range(t):
        j = 0
        while j < n-1:
            if(final_order[j] == 'B' and final_order[j+1] == 'G'):
                temp = final_order[j]
                final_order[j] = final_order[j+1]
                final_order[j+1] = temp
                j += 2
            else:
                j += 1

    res = "".join(final_order)
    print(res)