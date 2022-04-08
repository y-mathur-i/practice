"""
Print all subsequences
of string "ABCD"
"""
# method 1 powerset
def print_subsequence_bit(string: str) -> None:
    for i in range(0, 2**len(string)):# 2^len(string) as each char in string will be included or not
        curr_string = ""
        for j in range(len(string)):
            if i&(1<<j):#  check if current char on j will be selected
                curr_string+= string[j]
        print(curr_string)
        

def print_subsequence_recursive(string: str) -> None:
    idx = 0
    print_subsequence_recursive_helper(idx=idx, string=string, curr_str="")

def print_subsequence_recursive_helper(idx: int, string: str, curr_str: str) -> None:
    if idx >= len(string):
        print(curr_str)
        return
    print_subsequence_recursive_helper(idx+1, string, curr_str+string[idx])
    print_subsequence_recursive_helper(idx+1, string, curr_str)

if __name__=="__main__":
    string = "312"
    # print_subsequence_bit(string=string)
    print_subsequence_recursive(string)