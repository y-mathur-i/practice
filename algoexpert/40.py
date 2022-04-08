from typing import List


arr = [1, 2, 3]

def generate_powerset(arr: List[int]):
    len_powerset = pow(2, len(arr))
    result = []
    for i in range(len_powerset):
        temp = []
        for j in range(len(arr)):
            if i&(1<<j):
                temp.append(arr[j])
        result.append(temp)
    return result

print(generate_powerset(arr))