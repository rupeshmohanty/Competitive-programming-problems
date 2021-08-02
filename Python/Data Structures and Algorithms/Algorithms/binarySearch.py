# Binary Search - Works only for a sorted list!

# Linear Search!
def linear_search(numbers_list,number_to_find):
    for i in range(len(numbers_list)):
        if numbers_list[i] == number_to_find:
            return i
    
    return -1

# Binary search without recursion!
def binary_search(numbers_list,number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while(left_index <= right_index):
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    
    return -1

# Binary Search with recursion!
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
        
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index
    
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == "__main__":
    numbers_list = [12,15,17,19,21,24,45,67]
    number_to_find = 45

    index1 = binary_search(numbers_list, number_to_find)
    index2 = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)
    print(f"Position using binary search without recurstion {index1}")
    print(f"Position using binary search with recursion {index2}")

