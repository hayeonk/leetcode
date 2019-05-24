class Solution(object):
    def validPalindrome(self, s):
        def isPalindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                if isPalindrome(s[i:j]) or isPalindrome(s[i+1:j+1]):
                    return True
                else:
                    return False
            i += 1
            j -= 1
            
        return True