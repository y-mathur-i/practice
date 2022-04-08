import enum
from re import sub
from typing import List

# given and unsorted array [only part of it] find the size of sub array
# to sort that makes the array sorted
# [1, 2, 3, 4, 5, -1]
# so we need to find the smallest unsorted element and greatest unsorted element
# and their positions in the array if it were to be sorted


def subarray_sort(arr: List[int]):
    min_ele = float("inf")
    max_ele = float("-inf")
    for idx, ele in enumerate(arr):
        if not is_sorted(arr, idx):
            min_ele = min(ele, min_ele)
            max_ele = max(ele, max_ele)
    print(min_ele)
    print(max_ele)
    if min_ele == float("inf"):
        return -1,-1
    left = 0
    while arr[left] <= min_ele:
        left += 1
    right = len(arr) - 1
    while arr[right] >= max_ele:
        right -= 1
        
    print(left, right)
    return [left, right]

def is_sorted(arr: List[int], idx: int) -> bool:
    if (idx == 0 or arr[idx-1] <= arr[idx]) and (idx+1 == len(arr) or arr[idx] <= arr[idx+1]):
        return True
    return False 
    
arr = [1, 2, 3, 4, 5, -1]

subarray_sort(arr)

arr2 = [1, 2, 4, 7, 10 , 11, 7, 6, 12, 7, 16, 18, 19]

subarray_sort(arr2)
