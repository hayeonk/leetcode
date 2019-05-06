class Solution(object):
    def groupStrings(self, strings):
        def isSameGroup(s1, s2):
            if len(s1) != len(s2):
                return False
            
            if len(s1) == 1:
                return True
            
            diff = (ord(s2[0]) - ord(s1[0])) % 26
            for i in xrange(1, len(s1)):
                if (ord(s2[i]) - ord(s1[i])) % 26 != diff:
                    return False
            return True
        
        ans = []
        
        for s in strings:
            check = False
            for i in xrange(len(ans)):
                if isSameGroup(ans[i][0], s):
                    ans[i].append(s)
                    check = True
            if not check:
                ans.append([s])
        return ans