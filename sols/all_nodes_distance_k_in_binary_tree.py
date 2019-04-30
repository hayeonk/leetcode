# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
from collections import deque

class Solution(object):
    def distanceK(self, root, target, K):
        graph = defaultdict(dict)
        
        def makeGraph(root):
            if root.left:
                graph[root.val][root.left.val] = 1
                graph[root.left.val][root.val] = 1
                makeGraph(root.left)
            if root.right:
                graph[root.val][root.right.val] = 1
                graph[root.right.val][root.val] = 1
                makeGraph(root.right)
        
        makeGraph(root)
        q = deque([(target.val, 0)])
        visit = defaultdict(int)
        visit[target.val] = 1
        ans = []
        while q:
            u, d = q.popleft()
            if d > K:
                continue
            if d == K:
                ans.append(u)
            else:
                for v in graph[u]:
                    if not visit[v]:
                        q.append((v, d+1))
                        visit[v] = 1
        return ans