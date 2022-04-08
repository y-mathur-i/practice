from collections import defaultdict
from typing import List

# given a lost of strings group anagrams
# two strings are anagrams if they are equal in sorted form

def group_anagrams(array: List[str]):
    result = defaultdict(list)
    for word in array:
        sorted_word = "".join(sorted(list(word)))
        result[sorted_word].append(word)
    return list(value for value in result.values())

arr = ['yo', 'act', 'flop', 'tac', 'cat', 'oy', 'olfp']

print(group_anagrams(arr))
