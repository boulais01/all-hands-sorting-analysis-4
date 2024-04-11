"""Various sorting algorithms for testing our module."""

from typing import List

def noop(arr: List):
    pass

# Time complexity of O(n^2)
def bubble_sort(arr: List[int], n: int):
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Time complexity of O(n^2)
def bubble_sort_str(arr: List[str], n: int):
    temp = ""
    compare = lambda a, b: (a < b) - (a > b)
    # Sort string using the bubble sort
    for i in range(n-1):
        for j in range(i+1, n):
            if compare(arr[j], arr[i]) > 0:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

# Time complexity of O(n^2)
def selection_sort(arr, n):
    for s in range(n):
        min_idx = s
        for i in range(s + 1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i
        (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])

# Time complexity of O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        a = arr[i]
        j = i - 1
        while j >= 0 and a < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = a
    return arr

def heapify(nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


# Time complexity of O(n log(n))
def heap_sort(arr, n):
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Time complexity of O(n^2)
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

# Time complexity of O(n^2)
def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)

def merge(arr1,arr2):
    i=0
    j=0
    result=[]
    while(i<len(arr1) and j<len(arr2)):
        if arr2[j]>arr1[i]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    while(i<len(arr1)):
        result.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        result.append(arr2[j])
        j+=1
    return result

# Time complexity of O(n log(n))
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)
