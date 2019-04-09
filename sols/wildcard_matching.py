class Solution(object):
    def isMatch(self, s, p):
        m = [[-1] * (len(p) + 1) for _ in xrange(len(s) + 1)]
        
        def match(i, j):
            if m[i][j] != -1:
                return m[i][j]
            
            if i == len(s):
                m[i][j] = (j == len(p)) or (len(set(p[j:])) == 1 and p[j] == "*")
                return m[i][j]
            
            if j == len(p):
                m[i][j] = False
                return False
            
            if s[i] == p[j] or p[j] == "?":
                m[i][j] = match(i+1, j+1)
                return m[i][j]
            
            if p[j] == "*":
                for k in xrange(i, len(s) + 1):
                    if match(k, j+1):
                        m[i][j] = True
                        return True
            
            m[i][j] = False
            return False
        
        return match(0, 0)