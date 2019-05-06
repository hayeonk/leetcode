class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        ans = []
        
        prev = lower
        for n in nums:
            if n < prev:
                continue
            if n > upper:
                break
            
            if n == prev:
                prev += 1
            
            else:
                if prev == n-1:
                    ans.append(str(prev))
                else:
                    ans.append("->".join(map(str, [prev, n-1])))
                prev = n + 1
        
        if prev <= upper:
            if prev == upper:
                ans.append(str(prev))
            else:
                ans.append("->".join(map(str, [prev, upper])))
        return ans