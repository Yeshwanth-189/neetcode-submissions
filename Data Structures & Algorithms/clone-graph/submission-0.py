"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(curr: 'Node') -> 'Node':
            # If already cloned, return the clone
            if curr in old_to_new:
                return old_to_new[curr]

            # Create clone of current node
            clone = Node(curr.val)
            old_to_new[curr] = clone

            # Clone all neighbors and connect them
            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)