from typing import List
from random import shuffle

def quick_sort(arr: List[int]) -> None:
    quick_sort_helper(arr, 0, len(arr)-1)    
    
def quick_sort_helper(arr: List[int], left, right) -> None:
    if left < right:
        # splitting_idx = partition(arr, left, right)
        splitting_idx = hoare_partition(arr, left, right)
        quick_sort_helper(arr, left, splitting_idx - 1)
        quick_sort_helper(arr, splitting_idx + 1, right)


def partition(arr: List[int], left: int, right: int) -> None:
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            swap(i, j, arr)
    i += 1
    swap(i, right, arr)
    return i

def hoare_partition(arr: List[int], left: int, right: int) -> None:
    pivot = arr[left]
    pivot_idx = left
    left += 1
    while left <= right:
        if arr[left] > pivot and arr[right] < pivot:
            swap(left, right, arr)
        if arr[left] <= pivot:
            left += 1
        if arr[right] >= pivot:
            right -= 1
    swap(pivot_idx, right, arr)
    return right

def swap(left: int, right: int, arr: List[int]) -> None:
    arr[left], arr[right] = arr[right], arr[left]

arr = list(range(10))
shuffle(arr)
print(arr)
quick_sort(arr)
print(arr)

