class Solution(object):
    def findLongestWord(self, s, d):
        ans = ""
        for word in d:
            if len(word) < len(ans):
                continue
            
            i = j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            
            if i == len(word) and (len(word) > len(ans) or word < ans):
                ans = word
                
        return ans