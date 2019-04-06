from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        
        for c in ransomNote:
            if c not in magazine or magazine[c] < ransomNote[c]:
                return False
        return True