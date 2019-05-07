from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        C = Counter(s)
        
        return sum([1 for x in C if C[x] % 2]) <= 1