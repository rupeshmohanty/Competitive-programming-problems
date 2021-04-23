if __name__ == "__main__":
    t1 = input()
    t2 = input()

    converted_t1 = t1.lower()
    converted_t2 = t2.lower()

    if(converted_t1 == converted_t2):
        print(0)
    else:
        for i in range(len(t1)):
            if(converted_t1[i] > converted_t2[i]):
                print(1)
                break
            elif(converted_t1[i] < converted_t2[i]):
                print(-1)
                break
            else:
                continue