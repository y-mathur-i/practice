from typing import List


"""
This is an example based on a problem on leetcode
problem no 2192
-- all ancestors of a node in a DAG
        I found topologically sorted order of vertices and then 
        did dfs for each node on the graph based on that order
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
            graph[source].neighbours.append(dest)
            rev_graph[dest].append(source)

        for i in range(n):
            if i not in self.visited:
                self.__topo_sort(graph, i)
        parents = {}
        for v in self.res:
            done = set()
            self.__dfs(rev_graph, done, v)
            done.remove(v)
            parents[v] = sorted(done)
        return list(parents[k] for k in sorted(parents.keys()))

    def __topo_sort(self, graph, curr):
        for nei in graph[curr].neighbours:
            if nei not in self.visited:
                self.__topo_sort(graph, nei)
        self.visited.add(curr)
        self.res.append(curr)
    
    def __dfs(self, graph, done, curr):
        if curr not in done:
            done.add(curr)
            for nei in graph[curr]:
                self.__dfs(graph, done, nei)
