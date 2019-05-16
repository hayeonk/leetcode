from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts):
        group = []
        acountToGroup = {}
        acountToName = {}
        allAcount = set()
        
        def find(u):
            if group[u] != u:
                group[u] = find(group[u])
            return group[u]
        
        def union(u, v):
            u = find(u)
            v = find(v)
            
            if u != v:
                group[u] = v
        
        idx = 0
        for info in accounts:
            name = info[0]
            for acount in info[1:]:
                if acount not in acountToGroup:
                    acountToGroup[acount] = idx
                    group.append(idx)
                    idx += 1
                if acount not in acountToName:
                    acountToName[acount] = name
                
                allAcount.add(acount)
                
            for i in xrange(1, len(info)-1):
                union(acountToGroup[info[i]], acountToGroup[info[i+1]])
        
        groupToAcount = defaultdict(list)
        for acount in allAcount:
            u = find(acountToGroup[acount])
            groupToAcount[u].append(acount)
        
        ans = []
        for acounts in groupToAcount.values():
            name = acountToName[acounts[0]]
            l = [name]
            l += sorted(acounts)
            ans.append(l)
        return ans