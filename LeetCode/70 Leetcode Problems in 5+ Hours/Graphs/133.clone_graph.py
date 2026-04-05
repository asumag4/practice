"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Then use a queue (for DFS) to traverse the entire graph quickly
        def dfsGraph(node):

            nonlocal visited
            # print(visited)

            if (node in visited.keys()):
                return visited[node]
            
            nodeClone = Node(node.val) 
            visited[node] = nodeClone
            for nei in node.neighbors:
                nodeClone.neighbors.append(dfsGraph(nei))

            return nodeClone

        if (not node):
            return None

        visited = {}

        # Create a copy of the starter node
        clonedGraph = dfsGraph(node)
        # print(clonedGraph, visited)
        return clonedGraph


