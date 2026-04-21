"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None
        cloned = {}
        def dfs(cur):
            if cur in cloned:
                return cloned[cur]
            
            new_node = Node(cur.val)
            cloned[cur] = new_node
            for nei in cur.neighbors:
                new_node.neighbors.append(dfs(nei))
            return new_node
        return dfs(node)
