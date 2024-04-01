"""Various sorting algorithms for testing our module."""

from typing import List

# Time complexity of O(n^2)
def bubble_sort(arr: List[int]):
    n = len(arr)
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

# Time complexity of O(n^2 + n)
def selection_sort(arr: List[int]):
    # adding this here to keep uniform function signatures
    size = len(arr)
    for s in range(size):
        min_idx = s
        for i in range(s + 1, size):
            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])

# Time complexity of O(n^2)
def insertion_sort(list1: List[int]):
    # Outer loop to traverse on len(list1)
    for i in range(1, len(list1)):
        a = list1[i]
        # Move elements of list1[0 to i-1],
        # which are greater to one position
        # ahead of their current position
        j = i - 1 
        while j >= 0 and a < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = a
    return list1
