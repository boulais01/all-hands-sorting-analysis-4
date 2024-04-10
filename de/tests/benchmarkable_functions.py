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
