from collections import defaultdict
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        n = len(org)
        graph = defaultdict(set)
        for seq in seqs:
            for i in xrange(len(seq)):
                if seq[i] > n or seq[i] < 1:
                    return False
                if i == 0:
                    graph[seq[0]]
                else:
                    if seq[i] == seq[i-1]:
                        return False
                    graph[seq[i]].add(seq[i-1])
        
        def dfs(u, recStack):
            visit[u] = 1
            recStack.add(u)
            
            for v in graph[u]:
                if not visit[v]:
                    dfs(v, recStack)
                elif v in recStack:
                    return False
            ans.append(u)
            return True
        
        visit = [0] * (n+1)
        ans = []
        for i in xrange(1, n+1):
            if i in graph and not visit[i]:
                if not dfs(i, set()):
                    return False
        
        if len(ans) < n:
            return False
        
        ans = ans[::-1]
        for i in xrange(1, n):
            if ans[i] not in graph[ans[i-1]]:
                return False
        return True