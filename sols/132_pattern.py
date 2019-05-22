class Solution(object):
    def find132pattern(self, nums):
        ranges = []
        
        for n in nums:
            if not ranges:
                ranges.append([n, n])
            
            for s, e in ranges[::-1]:
                if s < n < e:
                    return True
                elif n <= s:
                    break
            
            if n > ranges[-1][1]:
                ranges[-1][1] = n
            elif n < ranges[-1][0]:
                ranges.append([n, n])
        return False