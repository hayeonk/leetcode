class Solution(object):
    def grayCode(self, n):
        def getCode(n):
            if n == 0:
                return ["0"]
            rest = getCode(n-1)
            reverse = reversed(rest)
            ret = [x + "0" for x in rest] + [x + "1" for x in reverse]
            return ret
        
        ret = getCode(n)
        ret = [int(x, 2) for x in ret]
        return ret