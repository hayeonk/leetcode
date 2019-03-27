class Solution(object):
    def reconstructQueue(self, people):
        n = len(people)
        people.sort(reverse=True)
        ret = [[] for _ in xrange(n)]
        
        for i in reversed(xrange(n)):
            h, k = people[i]
            idx = j = 0
            while idx < k:
                if not ret[j] or ret[j][0] >= h:
                    idx += 1
                j += 1
            while ret[j]:
                j += 1
            ret[j] = [h, k]
            
        return ret