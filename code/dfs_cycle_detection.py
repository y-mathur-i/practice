"""
Problem no 1361
validate if the graph is a binary tree
    - directed acyclic graph with each node having only two children
    -- conditions to check
        - in_deg == 1 for all except one node
        - no cycle(back edge) (as a directed graph don't need to check for parent)
        - dfs covers all the nodes
"""
from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = {i: [] for i in range(n)}
        in_deg = [0]*n
        for i in range(n):
            l = leftChild[i]
            r = rightChild[i]
            if l != -1:
                graph[i].append(l)
                in_deg[l] += 1
            if r != -1:
                graph[i].append(r)
                in_deg[r] += 1
        done = set()
        def has_cycle(curr):
            if curr in done:
                return True
            done.add(curr)
            for nei in graph[curr]:
                if has_cycle(nei):
                    return True
            return False
        
        if in_deg.count(0) > 1 or max(in_deg) > 1 or in_deg.count(0) == 0:
            return False
        start_node = None

        for idx, deg in enumerate(in_deg):
            if deg == 0:
                start_node = idx
                break

        if start_node is None:
            return False

        if has_cycle(start_node):
            return False
        
        return len(done) == n
        
        
        
        # if any(v >= 2 for v in in_deg.values()):
        #     return False
        # for i in range(n):
        #     for j in range(n):
        #         if graph[i][j] and graph[j][i]:
        #             return False
        # done = set()
        # times = {}
        # q = []
        # for i in range(n):
        #     if in_deg[i] == 0:
        #         q.append(i)
        # done = set()
        # while q:
        #     curr = q.pop(0)
        #     done.add(curr)
        #     for nei, conn in enumerate(graph[curr]):
        #         if conn:
        #             if nei in done:
        #                 print(nei)
        #                 return False
        #             q.append(nei)
        # return len(done) == n
