"""
Example from leetcode problem
binary lifting is storing 
result for 2^x for some condition

up[v][j] = 2^jth ancestor of v
Works in cases if parent is greater than child
for v = 0 to n-1:
    up[v][0] = parent[v]
    for j = 1 .. log-1:
        up[v][j] = up[ up[v][j-1] ][j-1]
    time and space O(n*logn(n))
    # up[v][1] = up[ up[v][0] ][0]
    # up[v][2] = up[ up[v][1] ][1]
    # ................
    
if want it to work where that order is not there
for v = 0 .. n-1:
    up[v][0] = parent[v]

for j = 1 .. log-1:
    up[v][0] = parent[v]
    for v = 0 to n-1:    
        up[v][j] = up[ up[v][j-1] ][j-1]
        
Here log = nearest power of 2 less than n 

For each node we get 
parents 2^ith for i in range(1, log)
    log is nearest integer to n (no of nodes) in power of 2
    This has the second case
    
"""
from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.nodes = n
        self.parents = parent
        self.log_n = self.__get_log(n) + 1
        self.up = [[0 for _ in range(self.log_n)] for _ in range(n)]
        self.__pre_process()

    def getKthAncestor(self, node: int, k: int) -> int:
        if not k:
            return node
        for i in range(self.log_n):
            if k&(1<<i):
                node = self.up[node][i]
                if node == -1:
                    break
        return node

    def __pre_process(self):
        for v in range(self.nodes):
            self.up[v][0] = self.parents[v]
        for j in range(1, self.log_n):
            for v in range(self.nodes):
                if self.up[v][j-1] == -1:
                    self.up[v][j] = -1
                else:
                    self.up[v][j] = self.up[ self.up[v][j-1] ][j-1]
#         for n in range(1, self.nodes):
#             self.up[n][0] = self.parents[n]
#             for j in range(1, self.log_n):
#                 self.up[n][j] = self.up[ self.up[n][j-1] ][j-1]


    def __get_log(self, n: int) -> int:
        log = 0
        while (1 << (log + 1)) <= n:
            log += 1
        return log

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)