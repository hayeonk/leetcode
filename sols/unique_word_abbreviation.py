from collections import defaultdict
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.d = defaultdict(list)
        for word in dictionary:
            if len(word) <= 2:
                self.d[word].append(word)
            else:
                abbr = word[0] + str(len(word)-2) + word[-1]
                self.d[abbr].append(word)
                
    def isUnique(self, word):
        if len(word) <= 2:
            return True
        abbr = word[0] + str(len(word)-2) + word[-1]
        return abbr not in self.d or (len(self.d[abbr]) == 1 and self.d[abbr][0] == word)

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)