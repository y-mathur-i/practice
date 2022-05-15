from typing import List

class Heap:
    def __init__(self, arr: List[int], heap_type: str = "max") -> None:
        if heap_type not in ["max", "min"]:
            raise ValueError("please provide valid heap type")
        self._heap = arr
        self.__comp = self.__min_comp if heap_type == "min" else self.__max_comp
        self.__heapify()
    
    def sift_down(self, idx: int) -> None:
        left = self.__get_left(idx)
        right = self.__get_right(idx)
        if left < len(self._heap) and self.__comp(self._heap[left], self._heap[idx]):
            largest = left
        else:
            largest = idx
        if right < len(self._heap) and self.__comp(self._heap[right], self._heap[largest]):
            largest = right
            
        if largest != idx:
            self.__swap(self._heap, idx, largest)
            self.sift_down(largest)
    
    def pop_top(self):
        self.__swap(self._heap, 0, len(self._heap)-1)
        ele = self._heap.pop()
        self.sift_down(0)
        return ele

    @staticmethod
    def __swap(arr : List[int], left: int, right: int) -> None:
        arr[left], arr[right] = arr[right], arr[left]
    
    def __min_comp(self, no_1: int, no_2: int) -> bool:
        return no_1 <= no_2
    
    def __max_comp(self, no_1: int, no_2: int) -> bool:
        return no_1 > no_2
    
    def __get_parent(self, idx: int) -> int:
        return idx//2
    
    def __get_left(self, idx: int) -> int:
        return 2*idx
        
    def __get_right(self, idx: int) -> int:
        return 2*idx + 1

    def __heapify(self) -> None:
        for i in reversed(range(len(self._heap))):
            self.sift_down(i)



arr = [4, 1, 3, 2, 16, 9, 10 , 14, 8, 7]

heap = Heap(arr)

print(heap._heap)

while heap._heap:
    print(heap.pop_top())
