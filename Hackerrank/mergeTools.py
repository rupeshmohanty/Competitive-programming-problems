def merge_the_tools(string, k):
    temp = []
    l = 0

    for i in range(len(string)):
        l += 1
        if string[i] not in temp:
            temp.append(string[i])

        if l == k:
            print("".join(str(e) for e in temp))
            temp = []
            l = 0

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)