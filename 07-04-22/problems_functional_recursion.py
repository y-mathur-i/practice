""" 
Reversing an array
using recursion
"""
from operator import truediv
from typing import List

def rev_arr_rec(arr: List[int]) -> None:
    if not arr:
        return
    curr = arr.pop(0)
    rev_arr_rec(arr)
    arr.append(curr)

def check_palin_rec(string: str, i: int):
    if i > len(string)//2:
        return True
    return string[i] == string[len(string)-i-1] and check_palin_rec(string , i+1)


if __name__=="__main__":
    # arr = [1, 2, 3, 4]
    # rev_arr_rec(arr)
    # print(arr)
    string = "aba"
    print(check_palin_rec(string, 0))