class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        i = j = num = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if not num and abbr[j] == "0":
                    return False
                num = 10 * num + int(abbr[j])
                j += 1
            
            elif num:
                i += num
                num = 0
            
            elif word[i] == abbr[j]:
                i += 1
                j += 1
            
            else:
                return False
        
        if num:
            i += num
        return i == len(word) and j == len(abbr)