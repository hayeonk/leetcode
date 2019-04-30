"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return node
        
        newNode = Node(node.val, [])
        visit = {}
        def dfs(newNode, node):
            visit[node] = newNode
            
            for nei in node.neighbors:
                if nei not in visit:
                    newNei = Node(nei.val, [])
                    newNode.neighbors.append(newNei)
                    dfs(newNei, nei)
                else:
                    newNode.neighbors.append(visit[nei])
                    
        dfs(newNode, node)
        return newNode
                    
                