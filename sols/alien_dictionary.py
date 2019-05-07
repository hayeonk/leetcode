from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        def buildGraph(w1, w2):
            i =  j =0
            while i < len(w1) and j < len(w2):
                if w1[i] != w2[j]:
                    graph[w1[i]].append(w2[i])
                    break
                else:
                    graph[w1[i]]
                i += 1
                j += 1
                
            while i < len(w1):
                graph[w1[i]]
                i += 1
            while j < len(w2):
                graph[w2[j]]
                j += 1
        
        graph = defaultdict(list)
        
        last = ""
        for i in xrange(len(words)):
            buildGraph(last, words[i])
            last = words[i]
        
        def dfs(u, recStack):
            visited.add(u)
            recStack.add(u)
            
            if u in graph:
                for v in graph[u]:
                    if v not in visited:
                        if not dfs(v, recStack):
                            return False
                    elif v in recStack:
                        return False
            
            recStack.remove(u)
            ans.append(u)
            return True
        
        ans = []
        visited = set()
        for c in graph:
            if c not in visited:
                if not dfs(c, set()):
                    return ""
                
        return "".join(ans[::-1])