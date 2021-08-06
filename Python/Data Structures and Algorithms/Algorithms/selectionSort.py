# Selection sort!
# Time complexity: O(n^2)
def selection_sort(elements):
    size = len(elements)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if elements[j] < elements[min_index]:
                min_index = j
        if i != min_index:
            elements[i],elements[min_index] = elements[min_index],elements[i]    

if __name__ == "__main__":
    elements = [78,12,15,8,61,53,23,27]
    selection_sort(elements)
    print(elements)