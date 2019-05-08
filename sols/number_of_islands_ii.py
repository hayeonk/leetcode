class Solution(object):
    def numIslands2(self, m, n, positions):
        d = {}
        idx = 0
        group = []
        rank = []
    
        def find(u):
            if group[u] != u:
                group[u] = find(group[u])
            return group[u]
    
        def union(u, v):
            u = find(u)
            v = find(v)
            
            if u != v:
                if rank[u] > rank[v]:
                    u, v = v, u
                    
                group[u] = v
                
                if rank[u] == rank[v]:
                    rank[v] += 1
                return 1
            return 0
        
        ans = []
        cnt = 0
        for i, j in positions:
            if (i, j) in d:
                ans.append(ans[-1])
                continue
                
            d[(i, j)] = idx
            group.append(idx)
            rank.append(1)
            idx += 1
            cnt += 1
            
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + di, j + dj
                if (ni, nj) in d:
                    cnt -= union(d[(i, j)], d[(ni, nj)])
                    
            #ans.append(len(set([find(x) for x in group])))
            ans.append(cnt)
        return ans