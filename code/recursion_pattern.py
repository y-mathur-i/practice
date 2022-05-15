""" 
Recusion problem patterns
"""
from typing import List

""" 
Print subsequences where sum is k
"""
def print_subsequence_sum_k(k: int, arr: List[int]):
    idx = 0
    print_subsequence_sum_k_helper(idx, k, arr, 0, [])
    
def print_subsequence_sum_k_helper(idx: int, k: int, arr: List[int], curr_sum: int, curr_seq):
    if curr_sum >= k:
        if curr_sum == k:
            print(curr_seq)
        return
    if idx >= len(arr):
        return
    print_subsequence_sum_k_helper(idx+1, k, arr, curr_sum+arr[idx], curr_seq+[arr[idx]])
    print_subsequence_sum_k_helper(idx+1, k, arr, curr_sum, curr_seq)

if __name__=="__main__":
    print_subsequence_sum_k(1, [1,2,1])
