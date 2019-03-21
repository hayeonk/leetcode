from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        words = defaultdict(list)
        for word in strs:
            words[tuple(sorted(word))].append(word)
        
        return words.values()
        