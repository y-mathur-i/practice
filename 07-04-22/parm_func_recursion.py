def sum_param(i: int, sum: int) -> None:
    if i < 1:
        print(sum)
        return
    sum_param(i-1, sum+i)

def sum_func(i: int) -> int:
    if i < 1:
        return 0
    return i + sum_func(i-1)
    
    
if __name__ == "__main__":
    i = 3
    sum = 0
    sum_param(i, sum)
    print(sum)
    print(sum_func(3))
