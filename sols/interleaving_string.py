class Solution(object):
    def __init__(self):
        self.m = {}
        
    def isInterleave(self, s1, s2, s3):
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        
        if (s1, s2, s3) in self.m:
            return self.m[(s1, s2, s3)]
        
        ans = False
        if s1[0] == s2[0] == s3[0]:
            ans = self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        
        elif s1[0] == s3[0]:
            ans = self.isInterleave(s1[1:], s2, s3[1:])
        
        elif s2[0] == s3[0]:
            ans = self.isInterleave(s1, s2[1:], s3[1:])
        
        self.m[(s1, s2, s3)] = ans
        return ans