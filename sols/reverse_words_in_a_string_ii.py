class Solution(object):
    def reverseWords(self, str):
        def reverse(str, lo, hi):
            while lo < hi:
                str[lo], str[hi] = str[hi], str[lo]
                lo += 1
                hi -= 1
                
        reverse(str, 0, len(str)-1)
        
        i = j = 0
        for j in xrange(len(str)):
            if str[j] == " ":
                reverse(str, i, j-1)
                i = j + 1
        reverse(str, i, j)
        
        