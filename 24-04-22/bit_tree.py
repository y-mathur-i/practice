class NumArray:

    def __init__(self, nums: List[int]):
        self.__size = len(nums)+1
        self.__bit_tree = [0 for _ in range(len(nums)+1)]
        self.__construct_arr(nums)
        self.__nums = nums
        
    def update(self, index: int, val: int) -> None:
        idx = index + 1
        delta = val - self.__nums[index]
        self.__nums[index] = val
        while idx < self.__size:
            self.__bit_tree[idx] += delta
            idx += (idx&-idx)

    def sumRange(self, left: int, right: int) -> int:
        first_sum = self.__sum_till_idx(right)
        second_sum = self.__sum_till_idx(left-1)
        return first_sum - second_sum

    def __construct_arr(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            idx = i + 1
            while idx < self.__size:
                self.__bit_tree[idx] += arr[i]
                idx += (idx&-idx)

    def __sum_till_idx(self, idx: int) -> int:
        pref_sum = 0
        idx += 1
        while idx > 0:
            pref_sum += self.__bit_tree[idx]
            idx -= (idx&-idx)
        return pref_sum
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
