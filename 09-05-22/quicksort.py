from typing import List
from random import shuffle

def quick_sort(arr: List[int]) -> None:
    quick_sort_helper(arr, 0, len(arr)-1)    
    
def quick_sort_helper(arr: List[int], left, right) -> None:
    if left < right:
        splitting_idx = partition(arr, left, right)
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

def swap(left: int, right: int, arr: List[int]) -> None:
    arr[left], arr[right] = arr[right], arr[left]

arr = list(range(10))
shuffle(arr)
print(arr)
quick_sort(arr)
print(arr)

