# Question 4 :
# create a function with the name check_prime which takes a number as input and checks if the given number is prime or composite. The function returns 1 if the number is prime,0 if the number is composite and 0 otherwise.

# create another function with the name prime_composite_list which takes a list of numbers and checks whether the numbers in the list are prime or composite. Include all th prime numbers in one list and all the composite numbers in another list. Create a 3rd list and include the list of prime numbers and the list of composite numbers in the 3rd list and return the 3rd list from this function. The third list should be a list of lists.

# Note : use the function check_prime to find whether the number is prime or composite.

# To test the code against your customized Input through console, please refer to the below instructions

# The first line in the sample input is the count of numbers to be provided in the input list
# The next few lines are the numbers to be included in the list provided one by one

# Sample Input :
# 4
# 11
# 7
# 90
# 44

# Expected Output :

# [[11, 7], [90, 44]]


# Please use the below main program code to implement and to test/run your code and submit the complete code along with this main code.

# if __name__=='__main__':
# inp=[]
# count=int(input())
# for i in range(count):
# inp.append(int(input()))
# print(check_prime(inp[1]))
# result=prime_composite_list(inp)
# print(result)

# Solution!
def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

def prime_composite_list(l):
    prime = []
    composite = []
    res = []

    for i in l:
        if check_prime(i):
            prime.append(i)
        else:
            composite.append(i)

    res.append(prime)
    res.append(composite)

    return res

if __name__=='__main__':
    inp=[]
    count=int(input())
    for i in range(count):
        inp.append(int(input())

    result=prime_composite_list(inp)
    print(result)