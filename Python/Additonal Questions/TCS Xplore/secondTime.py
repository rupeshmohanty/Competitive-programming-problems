# Write a Python program to find the position of the second occurrence of a given number in a given list of numbers.
# Function will take as input a list of numbers as first argument and a numeric variable as second argument . This function should return the index where the given variable value occurs in the list for the second time

# Function signature:
# getIndex(listOfIntegers,NumericVariable):

# In the above function signature, First argument represents list of integer values and
# Second argument represents a number, whose second occurred position(index) to be returned.
# The function should return the index of the number(supplied as second argument), occurred for the second time in the list.

# If the number does not occur for the second time in the input list or If the number does not exist in the list then the function should return 0.

# Develop a main program , with below sequence of actions:

# a. Create an empty list .
# b. Read the size of the list from standard input
# c. Based on the size of the list read above, repeat reading and adding the elements to the list created.
# d. Read the number, whose index is to be searched for its second occurrence .
# e. Then call getIndex function by supplying the input list as first argument and numeric value ( whose index is to be searched for its second occurrence) as second argument.
# Function should return the index of the second occurrence of the number(whose value supplied as second argument to the main program through numeric variable)
# Finally print the returned value of the function.

# Look at the Sample testcase below for more clarity to write the input and output statements in the main section.

# 1.Sample Testcase1#:
# Let us assume to create a list with 5 elements (3,4,3,7,4) and
# to search for the index of the second occurrence of 3 in the list

# Input :

# 5
# 3
# 4
# 3
# 7
# 4
# 3

# Output:
# 2

# Desctription:
# In the above Input, the first line content(5) represents the number of elements in the list, to be created
# From Second line to 6th line represents the 5 elements as below and to be added to the list created.
# 3
# 4
# 3
# 7
# 4

# The last line content (3) represents the number to search for its second occurance position(Index)
# in the input list

# Output is 2 means, the element 3 is found second time at the index value 2 , in the given input list.


# 2.Sample Testcase#2:
# Input:
# 4
# 2
# 3
# 4
# 5
# 5
# Output:
# 0

# Desctription:
# In the above Sample Input, the first line content(4) represents the number of elements in the list, to be created
# From Second line to 5th line represents the 4 elements as below and to be added to the list created.
# 2
# 3
# 4
# 5
# The last line content (5) represents the number to search for its second occurance position(Index) in the input list

# Output is 0 means, the element 5 is not found second time in the input list .

# Solution!

def getIndex(numList,a):
    arr = []

    for i in range(len(numList)):
        if numList[i] == a:
            arr.append(i)
    
    if len(arr) > 1:
        return arr[1]
    else:
        return 0

if __name__ == "__main__":
    l = []
    ele = int(input())
    for i in range(ele):
        l.append(int(input()))
    
    num = int(input())
    res = getIndex(l,num)
    print(res)