from random import shuffle
from tkinter import N
from typing import List


def merge_sort(arr: List[int]) -> None:
    return merge_sort_helper(arr)    

def merge_sort_helper(arr: List[int]) -> None:
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_helper(left)
        merge_sort_helper(right)
        l = r = a = 0
        # arr = []
        # while left and right:
        #     if left[0] < right[0]:
        #         arr.append(left.pop(0))
        #     else:
        #         arr.append(right.pop(0))
        # for n in left:
        #     arr.append(n)
        # for n in right:
        #     arr.append(n)
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[a] = left[l]
                l += 1
            else:
                arr[a] = right[r]
                r += 1
            a += 1
        while l < len(left):
            arr[a] = left[l]
            l += 1
            a += 1
        while r < len(right):
            arr[a] = right[r]
            r += 1
            a += 1
    return arr


arr = list(range(10))
shuffle(arr)
print(arr)
print(merge_sort(arr))
print(arr)
