from typing import List
from collections import deque

"""
This is an example based on a problem on leetcode
problem no 2192
-- all ancestors of a node in a DAG
    --- not really topo sort 
        had to reversed the graph and find all the ancestors
"""

class Vertex:
    def __init__(self):
        self.neighbours = []
        self.parent = []

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.visited = set()
        self.res = []
        graph = {vertex: Vertex() for vertex in range(n)}
        rev_graph = {vertex:[] for vertex in range(n)}
        for source, dest in edges:
            rev_graph[dest].append(source)

        parents = {}
        for v in range(n):
            done = set()
            self.__dfs(rev_graph, done, v)
            done.remove(v)
            parents[v] = sorted(done)
        return list(parents[k] for k in sorted(parents.keys()))
    
    def __dfs(self, graph, done, curr):
        if curr not in done:
            done.add(curr)
            for nei in graph[curr]:
                self.__dfs(graph, done, nei)
        
"""
Course schedule 1
Here we use kahn's algorithm to determine 
order at which we should take courses to satisfy pre reqs
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        pre_req = {i: 0 for i in range(numCourses)}
        for s, d in prerequisites:
            graph[d].append(s)
            pre_req[s] += 1
        q = deque()
        res = []
        # print(graph)
        # print(pre_req)
        for i in range(numCourses):
            if not pre_req[i]:
                q.append(i)
        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in graph[curr]:
                pre_req[nei] -= 1
                if not pre_req[nei]:
                    q.append(nei)
        return res
