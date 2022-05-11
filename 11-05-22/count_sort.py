from typing import List
from random import randint

def countSort(arr: List[int]) -> None:
    min_ele = min(arr)
    max_ele = max(arr)
    len_freq_arr = max_ele-min_ele + 1
    freq_arr = [0 for _ in range(len_freq_arr)]
    for n in arr:
        freq_arr[n-min_ele] += 1
    i = 0
    for idx, freq in enumerate(freq_arr):
        for _ in range(freq):
            arr[i] = min_ele + idx
            i += 1
    return arr

arr = [randint(1, 10) for _ in range(10)]
print(arr)
countSort(arr)
print(arr)