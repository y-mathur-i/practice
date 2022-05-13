from typing import List


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
        
        
        
        
        
        
        