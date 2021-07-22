if __name__ == "__main__":
    input_number = input()
    count = 0

    for i in range(len(input_number)):
        if(input_number[i] == '7' or input_number[i] == '4'):
            count = count + 1

    if(count == 7 or count == 4):
        print("YES")
    else:
        print("NO")