# Bubble sort logic!
# O(n^2)
def bubbleSort(arr):
    size = len(arr) - 1
    for i in range(size-1):
        swapped = False
        for j in range(size-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swapped = True
        if swapped == False:
            break

# Insertion sort logic!
# O(n^2)
def insertionSort(arr):
    for i in range(1,len(arr)):
        anchor = arr[i]
        j = i - 1
        while j>=0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = anchor

# Selection sort!
# O(n^2)
def selectionSort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(min_index+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

# Merge sort!
# O(nlogn)
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
     
    mergeSort(left)
    mergeSort(right)

    merge_two_sorted_arr(left,right,arr)

def merge_two_sorted_arr(l,r,arr):
    len_l = len(l)
    len_r = len(r)
    i = j = k = 0
    
    # adding the elements one after another alongwith check!
    while i < len_l and j < len_r:
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    
    while i < len_l:
        arr[k] = l[i]
        i += 1
        k += 1
    
    while j < len_r:
        arr[k] = r[j]
        j += 1
        k += 1

# Binary search!
# O(log n)
def binarySearch(arr,val,l,r):
    if r < l:
        return -1
    
    mid = (l+r) // 2

    if arr[mid] == val:
        return mid
    elif val < arr[mid]:
        return binarySearch(arr, val, l, mid-1)
    
    return binarySearch(arr, val, mid+1, r)

 