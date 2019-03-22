class Solution(object):
    def isPalindrome(self, s):
        i, j = -1, len(s)
        while i <= j:
            i += 1
            j -= 1
            while i <= j and not s[i].isalpha() and not s[i].isdigit():
                i += 1
            while i <= j and not s[j].isalpha() and not s[j].isdigit():
                j -= 1
            if i > j:
                break
            if s[i].lower() != s[j].lower():
                return False
        return True