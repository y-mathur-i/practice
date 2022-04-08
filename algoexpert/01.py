import re
from typing import List, Tuple



def two_sum(arr: List[int], target: int) -> Tuple[int, int]:
    arr.sort()
    left =0 
    right = len(arr) - 1
    while left < right:
        left_val = arr[left]
        right_val = arr[right]
        if left_val + right_val > target:
            right -= 1
        elif left_val + right_val < target:
            left += 1
        else:
            return [left_val, right_val]
    return [-1, -1]
    
    
arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(two_sum(arr, target))
