
def print_name_n_times(name: str, n: int) -> None:
    if n == 0:
        return 
    print(name)
    print_name_n_times(name, n-1)

def print_one_to_n(n: int) -> None:
    if n == 0:
        return
    print_one_to_n(n-1)
    print(n)

def print_n_to_one(n: int) -> None:
    if n == 0:
        return
    print(n)
    print_n_to_one(n-1)

if __name__ == "__main__":
    """
    Time complexity -: O(n) function is called by reducing n by one
    Space complexity -: O(n) call stack at max has n function calls in it
    """
    # print_name_n_times("Hi", 5)
    # print_one_to_n(5)
    print_n_to_one(5)
     