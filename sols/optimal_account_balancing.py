from collections import defaultdict, deque
class Solution(object):
    def minTransfers(self, transactions):
        def balance(nonZero):
            q = deque()
            q.append([[0], nonZero[0]])
            
            while q:
                idxList, curSum = q.popleft()
                if curSum == 0:
                    break
                
                for i in xrange(idxList[-1] + 1, len(nonZero)):
                    q.append([idxList + [i], curSum + nonZero[i]])
            
            nonZero = [nonZero[i] for i in xrange(len(nonZero)) if i not in idxList]
            return nonZero
            
        d = defaultdict(int)
        
        for x, y, c in transactions:
            d[x] -= c
            d[y] += c
            
        nonZero = [d[x] for x in d if d[x] != 0]
        ans = len(nonZero)
        
        while nonZero:
            nonZero = balance(nonZero)
            ans -= 1
        
        return ans