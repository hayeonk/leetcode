class Solution(object):
    def getFactors(self, n):
        ans = []
        
        def makeCombination(picked, n):
            if n == 1:
                if picked:
                    ans.append(picked)
                return
            
            start = 2 if not picked else picked[-1]
            end = n if picked else n - 1
            for i in xrange(start, end + 1):
                if n % i == 0:
                    makeCombination(picked + [i], n / i)
        
        makeCombination([], n)
        return ans