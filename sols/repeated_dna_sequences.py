from collections import Counter
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        C = Counter()
        ans = []
        
        for i in xrange(len(s)-9):
            C[s[i:i+10]] += 1
            if C[s[i:i+10]] == 2:
                ans.append(s[i:i+10])
        
        return ans