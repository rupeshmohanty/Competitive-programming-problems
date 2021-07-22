if __name__ == "__main__":
    a, b = map(int,input().split())

    for i in range(1,a+1):
        if(i % 2 == 0):
            if(i % 4 == 0):
                print('#','.'*(b-1),sep='')
            else: 
                print('.'*(b-1),end = '#\n')
        else:
            print('#'*b)